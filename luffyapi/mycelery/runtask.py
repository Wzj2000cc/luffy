from mycelery.sms.tasks import send_sms1,send_sms2
from mycelery.email.tasks import send_email

send_sms1.delay()
send_sms2.delay()
send_email.delay()