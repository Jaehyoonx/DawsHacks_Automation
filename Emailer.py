import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailerSender:
    def __init__(self):
        self._sender = "pr0tect.yo0ur.ldentity@gmail.com"
        self._password = "rbqz gwsm lelq oowy"
        self.receiver = None
        self.atacker = None

    def sendWarning(self):
        if self.receiver == self.atacker:
            return None
        # Build MIME message
        message = MIMEMultipart("alternative")
        message["From"] = f"ProtectYourIdentity <{self._sender}>"
        message["To"] = self.receiver
        message["Subject"] = "Warning"

        email_message = "This is a warning, someone used our website to try to look your email up. Please make sure that your infomation is protected. The email that tried to do this lookup was: " + self.atacker

        html_body = self.build_email("Warning", email_message)
        mime_text = MIMEText(html_body, "html")
        message.attach(mime_text)

        return self.try_catch_send(message, self.receiver)

    def try_catch_send(self, message, receiver):
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self._sender, self._password)
                server.sendmail(self._sender, receiver, message.as_string())
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def build_email(self, title, email_message):
        html = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background-color: #f9f9f9;
                        margin: 0;
                        padding: 0;
                    }}
                    .email-container {{
                        width: 100%;
                        padding: 20px;
                        display: flex;
                        justify-content: center;
                    }}
                    .content {{
                        background-color: #ffffff;
                        padding: 30px;
                        border-radius: 8px;
                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        max-width: 600px;
                        width: 100%;
                    }}
                    h1 {{
                        color: #2c3e50;
                        font-size: 24px;
                        margin-bottom: 20px;
                    }}
                    p {{
                        color: #555555;
                        font-size: 16px;
                        line-height: 1.5;
                    }}
                    .btn {{
                        background-color: #3498db;
                        color: #ffffff;
                        padding: 10px 20px;
                        text-decoration: none;
                        border-radius: 5px;
                        font-weight: bold;
                        display: inline-block;
                        margin-top: 20px;
                    }}
                    .footer {{
                        text-align: center;
                        margin-top: 30px;
                        color: #aaaaaa;
                        font-size: 14px;
                    }}
                    @media only screen and (max-width: 600px) {{
                        .content {{
                            padding: 20px;
                        }}
                        h1 {{
                            font-size: 20px;
                        }}
                        p {{
                            font-size: 14px;
                        }}
                        .btn {{
                            padding: 8px 16px;
                        }}
                    }}
                </style>
            </head>
            <body>
                <div class='email-container'>
                    <div class='content'>
                        <h1>{title}</h1>
                        <p>{email_message}</p>
                        <a href='#' class='btn'>Click Here</a>
                    </div>
                </div>
                <div class='footer'>
                    <p>We host a website that pretends to give people the info about the emails that they lookup, but we instead warn the people whose emails have been looked up</p>
                </div>
            </body>
        </html>
        """
        return html
    

em = EmailerSender()