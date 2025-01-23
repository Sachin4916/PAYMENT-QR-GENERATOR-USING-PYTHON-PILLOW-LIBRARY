import qrcode

#taking upi id as input
 
upi_id = input("enter your upi id= ");

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#defining the payments URL BASED 

phonepe_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#create qr3code ech app
phonepe_qr= qrcode.make(phonepe_url)
paytm_qr= qrcode.make(paytm_url)
googlepay_qr= qrcode.make(googlepay_url)

#save the qr code
phonepe_qr.save('phone_qr.png')
paytm_qr.save('paytm_qr.jpeg')
googlepay_qr.save('googlepay_qr.png')

#display the qr code show we need the pillow library
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()

