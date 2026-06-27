# Wafflegun-SWAG-1
# Description
The S.W.A.G (Stroop-Wafel-Assault-Gun) is the latest generation of food based arms. It is a tire driven stroopwafel launcher with an auto loading system. It uses two motors for the launch and a servo for the loader and runs on a Xiao RP2040. The wafflegun can be used to hand out stroopwafels to an entire group from a distance within the span of just a couple seconds.

# Assembly
TO assemble the S.W.A.G start off by ordering the pcb from any shop you prefer, although i will explain how i ordered it using JLCPCB. Log in to JLCPCB and the hit "Order Now". From there you will be asked to add the gerber ZIP file from the repo. This will give you everything you need and the board should load on the site. Dont change anything for the rest of the order process, just hit next after you've added the gerber files zip. Following this pay for your pcb and then you're all done with the pcb until its delivered to you.

It should look like this is JLCPCB:

<img width="1012" height="322" alt="image" src="https://github.com/user-attachments/assets/b144273d-753d-418d-8658-8f7b5defc039" />

When the pcb arrives grab a BD139 NPN-transistor and place it in the holes near the bottom if the pcb with the white part facing towards the inside of the pcb (pictued in example 1). Then Solder the legs of the transistor to the pcb from the bottom side while making sure no bridges are made (pictured in example 2). Then cut off the legs until the point they are soldered at (pictured in example 3)

Example 1:

<img width="857" height="700" alt="image" src="https://github.com/user-attachments/assets/4c17a8bc-8583-4a21-9643-d125d0b09185" />

Next grab all your curved pin headers, I used male dupont surved pin headers in my example because those were the ones i had, but i would recomend using female dupont curved pin headers. Both are fine so use whichever one you have but if you have to order them, order the female headers. You should have 3: 1 * 2 headers and 2: 1 * 3 headers. Put each of the pin headers in the hole that corresponds to the width (pictured in example 4). Then as with the transistor, solder each pin from the bottom side to the pcb (pictured in example 5).

Now here comes the hard part, were using a tiny 15K ohm SMD-0402 resistor. For the next two solders we will be using solder paste as its really the only way to get a solder this precise. I would also recomend using a magnfying glass at this point as this resistor is very small. Place two small bits of solder paste on the two pads on which we will solder the resistor (pictured in example 6). Then incredibly gently place the resistor on the two pads with the resistors black side facing up and use a heat gun to carefully melt the solder while making sure not to stay in one place too long as not to melt the pcb. The final result should look like example 7.

Next grab 


Kicad wiring schematic:

<img width="775" height="690" alt="image" src="https://github.com/user-attachments/assets/ad9b5f81-0a22-448d-8880-519c2a328dae" />
