# Wafflegun-SWAG-1
# Description
The S.W.A.G (Stroop-Wafel-Assault-Gun) is the latest generation of food based arms. It is a tire driven stroopwafel launcher with an auto loading system. It uses two motors for the launch and a servo for the loader and runs on a Xiao RP2040. The wafflegun can be used to hand out stroopwafels to an entire group from a distance within the span of just a couple seconds.

# Assembly
TO assemble the S.W.A.G start off by ordering the pcb from any shop you prefer, although i will explain how i ordered it using JLCPCB. Log in to JLCPCB and the hit "Order Now". From there you will be asked to add the gerber ZIP file from the repo. This will give you everything you need and the board should load on the site. Dont change anything for the rest of the order process, just hit next after you've added the gerber files zip. Following this pay for your pcb and then you're all done with the pcb until its delivered to you.

It should look like this is JLCPCB:

<img width="1012" height="322" alt="image" src="https://github.com/user-attachments/assets/b144273d-753d-418d-8658-8f7b5defc039" />

Note: I will be refering to the side of the pcb with the letters as the top and from there i call the other sides left, right and bottom. This is also diferent from the side of the pcb as in the working layer.

When the pcb arrives grab a BD139 NPN-transistor and place it in the holes near the left side if the pcb with the white part facing towards the inside of the pcb (pictued in example 1). Then Solder the legs of the transistor to the pcb from the bottom side while making sure no bridges are made (pictured in example 2). Then cut off the legs until the point they are soldered at (pictured in example 3)

Example 1:

<img width="857" height="700" alt="image" src="https://github.com/user-attachments/assets/4c17a8bc-8583-4a21-9643-d125d0b09185" />

Example 2:

<img width="437" height="296" alt="image" src="https://github.com/user-attachments/assets/13a03622-fdef-4c62-b3d2-20c1d83505d4" />

Example 3:

<img width="315" height="135" alt="image" src="https://github.com/user-attachments/assets/6aa0c3cf-ff73-46a8-a697-a9236c12ab22" />


Next grab all your curved pin headers, I used male dupont surved pin headers in my example because those were the ones i had, but i would recomend using female dupont curved pin headers. Both are fine so use whichever one you have but if you have to order them, order the female headers. You should have 3: 1 * 2 headers and 2: 1 * 3 headers. Put each of the pin headers in the hole that corresponds to the width (pictured in example 4). Then as with the transistor, solder each pin from the bottom side to the pcb (pictured in example 5).

Example 4:

<img width="437" height="198" alt="image" src="https://github.com/user-attachments/assets/7eea082f-64b1-4733-88d5-0d7a1c3effb6" />

Example 5:

<img width="443" height="477" alt="image" src="https://github.com/user-attachments/assets/65f53e8a-bd30-4a07-b72f-07276d95e908" />

Now here comes the hard part, were using a tiny 1.5K ohm SMD-0402 resistor. For the next two solders we will be using solder paste as its really the only way to get a solder this precise. I would also recomend using a magnfying glass at this point as this resistor is very small. Place two small bits of solder paste on the two pads on which we will solder the resistor (pictured in example 6). Then incredibly gently place the resistor on the two pads with the resistors black side facing up and use a heat gun to carefully melt the solder while making sure not to stay in one place too long as not to melt the pcb. The final result should look like example 7.

Example 6:

<img width="333" height="252" alt="image" src="https://github.com/user-attachments/assets/f2b29d61-1ec7-4195-a458-d407c6de59ad" />

Example 7:

<img width="443" height="438" alt="image" src="https://github.com/user-attachments/assets/ec98a3e2-25cd-49ac-9724-0b421852060c" />

Lastly grab your solder paste again, and place a small glob on each of the solder pads for XIAO RP2040 (pictured in example 8). Then carefully place the XIAO RP2040 on top of the pads making sure each connection lines up with the micro-usb port facing towards the right side of the pcb (pictured in example 9). Then gently move the heatgun over the pcb to melt the solder while making sure not to melt the pcb or any other nearby components. The final result should look like example 9.

Example 8:

<img width="545" height="518" alt="image" src="https://github.com/user-attachments/assets/10842b48-459c-46e0-ae73-60ea2fa68ee2" />
ELFR1021
Example 9:

<img width="1152" height="2048" alt="image" src="https://github.com/user-attachments/assets/b47ce839-1b3e-410f-8f7a-b444575a53ca" />

You are now done with making the PCB for S.W.A.G-1

Kicad wiring schematic of the pcb:

<img width="894" height="456" alt="image" src="https://github.com/user-attachments/assets/28aee72e-5bb3-4bb5-9584-96d43ded699e" />

Kicad wiring schematic of the full circuit:

<img width="1096" height="561" alt="image" src="https://github.com/user-attachments/assets/b55f7ca6-2ae4-4be0-a16a-2104c1036110" />

To build the rest of the cuircuit start by grabbing your ELFR1021 DC high speed motors and cutting off the connector that is attached. After this crimp a dupont header on each wire of both of the motors. If you have used Female headers on the pcb, use male headers on the motors. If you have used male headers (like me) on the pcb use female headers on the motors. 

It should look like this:

<img width="1152" height="2048" alt="image" src="https://github.com/user-attachments/assets/5cff2bb6-a3b1-467e-80d2-e368698c38f6" />

After this attach red wire of both motors to the pinheaders group 5 on the pcb, and the black wires to the pinheader group 3 on the pcb.

It should look like this:

<img width="446" height="222" alt="image" src="https://github.com/user-attachments/assets/a3dc865a-10f5-4fb4-a79e-1119bddd168c" />





