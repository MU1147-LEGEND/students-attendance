from base64 import b64decode, b64encode

string = '''
import datetime
import os.path
import os
from cryptography.fernet import Fernet
import datetime

# if os.path.isfile('license.pixel'):
#     # Read the expiration date from the license file
#     with open('license.pixel', 'r') as f:
#         expiration_date = datetime.datetime.strptime(f.read().strip(), '%Y-%m-%d').date()

#     # get the current date
#     current_date = datetime.date.today()

#     # check if the current date is after the expiration date
#     if current_date > expiration_date:
#         print("This License has expired and can no longer be used.")
#         try:
#             os.remove('license.pixel')
#             print("No license file detected.")
#         except OSError:
#             print("error:No license file detected")
#         print("For License please contact at +8801734906838")
#         exit()


# Load the encryption key from the file
with open('license\encryption_key.sniper', 'rb') as f:
    key = f.read()

# Initialize the Fernet cipher with the encryption key
cipher = Fernet(key)

# Read the contents of the encrypted text file
with open('license\license.pixel', 'rb') as f:
    ciphertext = f.read()

# Decrypt the ciphertext using the Fernet cipher
plaintext = cipher.decrypt(ciphertext)

# Write the decrypted data to a temporary file
with open('license\license.txt', 'wb') as f:
    f.write(plaintext)

# Read the expiration date from the temporary file
with open('license\license.txt', 'r') as f:
    expiration_date = datetime.datetime.strptime(f.read().strip(), '%Y-%m-%d').date()

# Delete the temporary file
os.remove('license\license.txt')

# Check if the license has expired
today = datetime.date.today()
if today > expiration_date:
    print("License expired or Trial is end, Please contact at +8801734906838")
    exit(1)
else:
    # continue running the program normally
    import requests
    import pytz
    from twilio.rest import Client

    # # Your Account SID and Auth Token from twilio.com/console
    # account_sid = 'AC72f6db2fe3aa5013f1bf29fe725df7e6'
    # auth_token = 'e5b3abae6304cdac8f7fac8e48557f66'

    # # Initialize the Twilio client
    # client = Client(account_sid, auth_token)


    # Load student data from file
    with open('students.txt', 'r') as f:
        students = [line.strip().split(', ') for line in f]

    # Record attendance
    present = []
    tz = pytz.timezone('Asia/Dhaka')
    for name_id in students:
        name = name_id[0]
        id = name_id[1]
        now = datetime.datetime.now(tz)
        response = input(f"Is {name},{id} present? (y/n): ")
        if response.lower() == 'y':
            present.append((name, id, now.strftime('%Y-%m-%d %H:%M')))

    # Write attendance to file
    with open('attendance.txt', 'w') as f:
        for attendance in present:
            f.write(', '.join(attendance) + "\\n")

    # Find absent students
    absent = [(name, id, guardian_name, phone) for name, id, guardian_name, phone in students if (name, id) not in [(p[0], p[1]) for p in present]]

    # Write absent students to file
    with open('absent.txt', 'w') as f:
        for name, id, guardian_name, phone in absent:
            f.write(f"{name}, {id},{guardian_name},{phone}, {now.strftime('%Y-%m-%d %H:%M')}\\n")

    # # Send SMS notifications to absent students via API (twilio)
    # for name, id, guardian_name, phone in absent:
    #     message = f'Hello {guardian_name}, your child {name} with ID {id} was absent from school today.'
    #     message = client.messages.create(
    #         body=message,
    #         from_='+15673132923',
    #         to=phone
    #     )
    #     print(f'Sent SMS to {guardian_name} at {phone} with SID {message.sid}')

    # Send SMS notifications to absent students via API (sms.net.bd)
    url = "https://api.sms.net.bd/sendsms"
    api_key = "FdnavsH4Y0250QCTcyf5RO5lQE3rx2Og9982xjqo"
    for name, id, guardian_name, phone in absent:
        msg = f'Hello {guardian_name}, your child {name} with ID {id} was absent from school today.'
        payload = {
        "api_key": api_key,
        "to": phone,
        "msg": msg
    }
        response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Message Report:", response.text)
    else:
        print("Message Report:", response.text)
'''

data=b'CmltcG9ydCBkYXRldGltZQppbXBvcnQgb3MucGF0aAppbXBvcnQgb3MKZnJvbSBjcnlwdG9ncmFwaHkuZmVybmV0IGltcG9ydCBGZXJuZXQKaW1wb3J0IGRhdGV0aW1lCgojIGlmIG9zLnBhdGguaXNmaWxlKCdsaWNlbnNlLnBpeGVsJyk6CiMgICAgICMgUmVhZCB0aGUgZXhwaXJhdGlvbiBkYXRlIGZyb20gdGhlIGxpY2Vuc2UgZmlsZQojICAgICB3aXRoIG9wZW4oJ2xpY2Vuc2UucGl4ZWwnLCAncicpIGFzIGY6CiMgICAgICAgICBleHBpcmF0aW9uX2RhdGUgPSBkYXRldGltZS5kYXRldGltZS5zdHJwdGltZShmLnJlYWQoKS5zdHJpcCgpLCAnJVktJW0tJWQnKS5kYXRlKCkKCiMgICAgICMgZ2V0IHRoZSBjdXJyZW50IGRhdGUKIyAgICAgY3VycmVudF9kYXRlID0gZGF0ZXRpbWUuZGF0ZS50b2RheSgpCgojICAgICAjIGNoZWNrIGlmIHRoZSBjdXJyZW50IGRhdGUgaXMgYWZ0ZXIgdGhlIGV4cGlyYXRpb24gZGF0ZQojICAgICBpZiBjdXJyZW50X2RhdGUgPiBleHBpcmF0aW9uX2RhdGU6CiMgICAgICAgICBwcmludCgiVGhpcyBMaWNlbnNlIGhhcyBleHBpcmVkIGFuZCBjYW4gbm8gbG9uZ2VyIGJlIHVzZWQuIikKIyAgICAgICAgIHRyeToKIyAgICAgICAgICAgICBvcy5yZW1vdmUoJ2xpY2Vuc2UucGl4ZWwnKQojICAgICAgICAgICAgIHByaW50KCJObyBsaWNlbnNlIGZpbGUgZGV0ZWN0ZWQuIikKIyAgICAgICAgIGV4Y2VwdCBPU0Vycm9yOgojICAgICAgICAgICAgIHByaW50KCJlcnJvcjpObyBsaWNlbnNlIGZpbGUgZGV0ZWN0ZWQiKQojICAgICAgICAgcHJpbnQoIkZvciBMaWNlbnNlIHBsZWFzZSBjb250YWN0IGF0ICs4ODAxNzM0OTA2ODM4IikKIyAgICAgICAgIGV4aXQoKQoKCiMgTG9hZCB0aGUgZW5jcnlwdGlvbiBrZXkgZnJvbSB0aGUgZmlsZQp3aXRoIG9wZW4oJ2xpY2Vuc2VcZW5jcnlwdGlvbl9rZXkuc25pcGVyJywgJ3JiJykgYXMgZjoKICAgIGtleSA9IGYucmVhZCgpCgojIEluaXRpYWxpemUgdGhlIEZlcm5ldCBjaXBoZXIgd2l0aCB0aGUgZW5jcnlwdGlvbiBrZXkKY2lwaGVyID0gRmVybmV0KGtleSkKCiMgUmVhZCB0aGUgY29udGVudHMgb2YgdGhlIGVuY3J5cHRlZCB0ZXh0IGZpbGUKd2l0aCBvcGVuKCdsaWNlbnNlXGxpY2Vuc2UucGl4ZWwnLCAncmInKSBhcyBmOgogICAgY2lwaGVydGV4dCA9IGYucmVhZCgpCgojIERlY3J5cHQgdGhlIGNpcGhlcnRleHQgdXNpbmcgdGhlIEZlcm5ldCBjaXBoZXIKcGxhaW50ZXh0ID0gY2lwaGVyLmRlY3J5cHQoY2lwaGVydGV4dCkKCiMgV3JpdGUgdGhlIGRlY3J5cHRlZCBkYXRhIHRvIGEgdGVtcG9yYXJ5IGZpbGUKd2l0aCBvcGVuKCdsaWNlbnNlXGxpY2Vuc2UudHh0JywgJ3diJykgYXMgZjoKICAgIGYud3JpdGUocGxhaW50ZXh0KQoKIyBSZWFkIHRoZSBleHBpcmF0aW9uIGRhdGUgZnJvbSB0aGUgdGVtcG9yYXJ5IGZpbGUKd2l0aCBvcGVuKCdsaWNlbnNlXGxpY2Vuc2UudHh0JywgJ3InKSBhcyBmOgogICAgZXhwaXJhdGlvbl9kYXRlID0gZGF0ZXRpbWUuZGF0ZXRpbWUuc3RycHRpbWUoZi5yZWFkKCkuc3RyaXAoKSwgJyVZLSVtLSVkJykuZGF0ZSgpCgojIERlbGV0ZSB0aGUgdGVtcG9yYXJ5IGZpbGUKb3MucmVtb3ZlKCdsaWNlbnNlXGxpY2Vuc2UudHh0JykKCiMgQ2hlY2sgaWYgdGhlIGxpY2Vuc2UgaGFzIGV4cGlyZWQKdG9kYXkgPSBkYXRldGltZS5kYXRlLnRvZGF5KCkKaWYgdG9kYXkgPiBleHBpcmF0aW9uX2RhdGU6CiAgICBwcmludCgiTGljZW5zZSBleHBpcmVkIG9yIFRyaWFsIGlzIGVuZCwgUGxlYXNlIGNvbnRhY3QgYXQgKzg4MDE3MzQ5MDY4MzgiKQogICAgZXhpdCgxKQplbHNlOgogICAgIyBjb250aW51ZSBydW5uaW5nIHRoZSBwcm9ncmFtIG5vcm1hbGx5CiAgICBpbXBvcnQgcmVxdWVzdHMKICAgIGltcG9ydCBweXR6CiAgICBmcm9tIHR3aWxpby5yZXN0IGltcG9ydCBDbGllbnQKCiAgICAjICMgWW91ciBBY2NvdW50IFNJRCBhbmQgQXV0aCBUb2tlbiBmcm9tIHR3aWxpby5jb20vY29uc29sZQogICAgIyBhY2NvdW50X3NpZCA9ICdBQzcyZjZkYjJmZTNhYTUwMTNmMWJmMjlmZTcyNWRmN2U2JwogICAgIyBhdXRoX3Rva2VuID0gJ2U1YjNhYmFlNjMwNGNkYWM4ZjdmYWM4ZTQ4NTU3ZjY2JwoKICAgICMgIyBJbml0aWFsaXplIHRoZSBUd2lsaW8gY2xpZW50CiAgICAjIGNsaWVudCA9IENsaWVudChhY2NvdW50X3NpZCwgYXV0aF90b2tlbikKCgogICAgIyBMb2FkIHN0dWRlbnQgZGF0YSBmcm9tIGZpbGUKICAgIHdpdGggb3Blbignc3R1ZGVudHMudHh0JywgJ3InKSBhcyBmOgogICAgICAgIHN0dWRlbnRzID0gW2xpbmUuc3RyaXAoKS5zcGxpdCgnLCAnKSBmb3IgbGluZSBpbiBmXQoKICAgICMgUmVjb3JkIGF0dGVuZGFuY2UKICAgIHByZXNlbnQgPSBbXQogICAgdHogPSBweXR6LnRpbWV6b25lKCdBc2lhL0RoYWthJykKICAgIGZvciBuYW1lX2lkIGluIHN0dWRlbnRzOgogICAgICAgIG5hbWUgPSBuYW1lX2lkWzBdCiAgICAgICAgaWQgPSBuYW1lX2lkWzFdCiAgICAgICAgbm93ID0gZGF0ZXRpbWUuZGF0ZXRpbWUubm93KHR6KQogICAgICAgIHJlc3BvbnNlID0gaW5wdXQoZiJJcyB7bmFtZX0se2lkfSBwcmVzZW50PyAoeS9uKTogIikKICAgICAgICBpZiByZXNwb25zZS5sb3dlcigpID09ICd5JzoKICAgICAgICAgICAgcHJlc2VudC5hcHBlbmQoKG5hbWUsIGlkLCBub3cuc3RyZnRpbWUoJyVZLSVtLSVkICVIOiVNJykpKQoKICAgICMgV3JpdGUgYXR0ZW5kYW5jZSB0byBmaWxlCiAgICB3aXRoIG9wZW4oJ2F0dGVuZGFuY2UudHh0JywgJ3cnKSBhcyBmOgogICAgICAgIGZvciBhdHRlbmRhbmNlIGluIHByZXNlbnQ6CiAgICAgICAgICAgIGYud3JpdGUoJywgJy5qb2luKGF0dGVuZGFuY2UpICsgIlxuIikKCiAgICAjIEZpbmQgYWJzZW50IHN0dWRlbnRzCiAgICBhYnNlbnQgPSBbKG5hbWUsIGlkLCBndWFyZGlhbl9uYW1lLCBwaG9uZSkgZm9yIG5hbWUsIGlkLCBndWFyZGlhbl9uYW1lLCBwaG9uZSBpbiBzdHVkZW50cyBpZiAobmFtZSwgaWQpIG5vdCBpbiBbKHBbMF0sIHBbMV0pIGZvciBwIGluIHByZXNlbnRdXQoKICAgICMgV3JpdGUgYWJzZW50IHN0dWRlbnRzIHRvIGZpbGUKICAgIHdpdGggb3BlbignYWJzZW50LnR4dCcsICd3JykgYXMgZjoKICAgICAgICBmb3IgbmFtZSwgaWQsIGd1YXJkaWFuX25hbWUsIHBob25lIGluIGFic2VudDoKICAgICAgICAgICAgZi53cml0ZShmIntuYW1lfSwge2lkfSx7Z3VhcmRpYW5fbmFtZX0se3Bob25lfSwge25vdy5zdHJmdGltZSgnJVktJW0tJWQgJUg6JU0nKX1cbiIpCgogICAgIyAjIFNlbmQgU01TIG5vdGlmaWNhdGlvbnMgdG8gYWJzZW50IHN0dWRlbnRzIHZpYSBBUEkgKHR3aWxpbykKICAgICMgZm9yIG5hbWUsIGlkLCBndWFyZGlhbl9uYW1lLCBwaG9uZSBpbiBhYnNlbnQ6CiAgICAjICAgICBtZXNzYWdlID0gZidIZWxsbyB7Z3VhcmRpYW5fbmFtZX0sIHlvdXIgY2hpbGQge25hbWV9IHdpdGggSUQge2lkfSB3YXMgYWJzZW50IGZyb20gc2Nob29sIHRvZGF5LicKICAgICMgICAgIG1lc3NhZ2UgPSBjbGllbnQubWVzc2FnZXMuY3JlYXRlKAogICAgIyAgICAgICAgIGJvZHk9bWVzc2FnZSwKICAgICMgICAgICAgICBmcm9tXz0nKzE1NjczMTMyOTIzJywKICAgICMgICAgICAgICB0bz1waG9uZQogICAgIyAgICAgKQogICAgIyAgICAgcHJpbnQoZidTZW50IFNNUyB0byB7Z3VhcmRpYW5fbmFtZX0gYXQge3Bob25lfSB3aXRoIFNJRCB7bWVzc2FnZS5zaWR9JykKCiAgICAjIFNlbmQgU01TIG5vdGlmaWNhdGlvbnMgdG8gYWJzZW50IHN0dWRlbnRzIHZpYSBBUEkgKHNtcy5uZXQuYmQpCiAgICB1cmwgPSAiaHR0cHM6Ly9hcGkuc21zLm5ldC5iZC9zZW5kc21zIgogICAgYXBpX2tleSA9ICJGZG5hdnNINFkwMjUwUUNUY3lmNVJPNWxRRTNyeDJPZzk5ODJ4anFvIgogICAgZm9yIG5hbWUsIGlkLCBndWFyZGlhbl9uYW1lLCBwaG9uZSBpbiBhYnNlbnQ6CiAgICAgICAgbXNnID0gZidIZWxsbyB7Z3VhcmRpYW5fbmFtZX0sIHlvdXIgY2hpbGQge25hbWV9IHdpdGggSUQge2lkfSB3YXMgYWJzZW50IGZyb20gc2Nob29sIHRvZGF5LicKICAgICAgICBwYXlsb2FkID0gewogICAgICAgICJhcGlfa2V5IjogYXBpX2tleSwKICAgICAgICAidG8iOiBwaG9uZSwKICAgICAgICAibXNnIjogbXNnCiAgICB9CiAgICAgICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5wb3N0KHVybCwgZGF0YT1wYXlsb2FkKQogICAgaWYgcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjAwOgogICAgICAgIHByaW50KCJNZXNzYWdlIFJlcG9ydDoiLCByZXNwb25zZS50ZXh0KQogICAgZWxzZToKICAgICAgICBwcmludCgiTWVzc2FnZSBSZXBvcnQ6IiwgcmVzcG9uc2UudGV4dCkK'

def hide(s):
    return b64encode(s.encode('utf-8'))

def sniper(b):
    return b64decode(b).decode('utf-8')

# print(sniper(data))

eval(compile(sniper(data),'<string>', 'exec'))


