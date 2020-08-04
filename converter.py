from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__)
import os, time
from pathlib import Path
import concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)

@app.route('/', methods=['GET', 'POST'])
def submit_job():
    print("I'm here")
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        print('form', request.form)
        key = Path(request.files['video'].filename).stem + '-' + str(time.time())
        os.mkdir(key)
        request.files['video'].save(os.path.join(key, request.files['video'].filename))
        print('files', request.files)
        print(request.url_root)
        executor.submit(convert_video, key, request.files['video'].filename, request.form['email'])
        return render_template('success.html', file=request.files['video'].filename, email=request.form.get('email', 'None'))

def convert_video(directory, file, email):
    print(directory, file, request.url_root)
    os.system(f'cd {directory}; cp ../video-countdown/* .; cp {file} announcements.mp4; bash main.sh; mv fade_vid.mp4 {directory}-converted.mp4')
    print('done!')
    ## TODO: send an email with the right link to access the converted file
    link_url = os.path.join(request.url_root, 'converted', directory, f'{directory}-converted.mp4')
    print('link url', link_url)
    send_email(email, link_url)
    return True

def send_email(receiver_email, link):
    import smtplib, ssl

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "scubashanko@gmail.com"
    password = 'gbgapokntztqajrc'

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Your file has been converted"
        msg['From'] = sender_email
        msg['To'] = receiver_email
        
        # Create the message (HTML).
        html = f"""\
        Please download your file at {link}
        """

        # Record the MIME type - text/html.
        part1 = MIMEText(html, 'html')

        # Attach parts into message container
        msg.attach(part1)

        server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

@app.route('/converted/<path:directory>/<path:filename>')
def download_file(directory, filename):
    #return send_from_directory(directory, filename)
    #return "hello"
    print(request.url_root)
    print(directory, filename)
    return send_from_directory(directory, filename, as_attachment=True)
