import sys, webbot

endereco = " ".join(sys.argv[1:])

web = webbot.Browser()

web.go_to(f"https://www.google.com/maps/place/{endereco}")

