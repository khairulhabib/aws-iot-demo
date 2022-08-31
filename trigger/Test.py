from gpiozero import LED


led = LED(17) # red
led2 = LED(27) # green
led3 = LED(26) # yellow


led_list = [led,led2,led3]

def blink(dur,iter,idx):
    for x in range(iter):
        led_list[idx].on()
        time.sleep(dur)
        led_list[idx].off()
        time.sleep(0.1)

blink(0.3,3,0)
blink(0.3,3,1)
blink(0.3,3,2)
