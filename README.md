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

Next take your SG90 servo and attach it to pinheader group 2 on the pcb with the brown wire of the servo (GND wire) being attached to the right-sided pin on pinheader group 2. If the brown wire is on the right pin, the red and yellow wire are too.

It should look like this:

<img width="451" height="367" alt="image" src="https://github.com/user-attachments/assets/0404f6f7-08d6-4042-ad3d-2c8efc86fa74" />

Following this i dont have a good physical example for the buttons. In the wiring diagram i show a SW-SP3T three way switch where one position is floating so no signal goes through the buttons meaning no part is turned on, and the other two positions going to either the motor or the servo so you can toggle the motor and servo separately. I do not have an SW_SP3T available due to a shipping error so the best i can do is show how to connect it. 

-First connect the right pin on pin header group 4 to the COM Pin ( also knows as the common pin and pin 3 on the wiring diagram showed earlier.). The brown wire is the wire you would connect to the common pin of the SW_SP3T.

<img width="461" height="420" alt="image" src="https://github.com/user-attachments/assets/006e4a92-01bd-49fd-902c-f1032e136aa0" />

-Then connect output 1 on the SW-SP3T to the middle pin on pinheader group 4 on the pcb and connect output 2 on the SW-SP3T to the left pin on pinheader group 4 on the pcb.

-Ouput 3 will be left floating as that will be the "off" pin so it has no output.

If you do all of this you can switch between turning on the servo, turning on the motor & having both off.

Next up take your 4*AA battery holder and if necessary crimp on female dupont headers to both wires if you have male headers on your pcb and male headers to both wires if you have female headers on your pcb.

It should look like this:
<img width="427" height="458" alt="image" src="https://github.com/user-attachments/assets/a589a4da-e58c-4911-bbf6-26b607fac032" />

Then attach the red wire to specifically the right-sided pin on pin header ground 1 on the pcb, and the black wire to the lift sided pin  on pin header ground 1 on the pcb.

It should look like this:

<img width="427" height="458" alt="image" src="https://github.com/user-attachments/assets/fca0a492-b0cc-4d62-bb90-e92798da3461" />

With this all the wiring is done! Now on to the 3D-printed parts.

Start by printing all of the pieces in the STL files folder. The gear pieces need to be printed twice but all of the other pieces need to be printed only once.

Start by grabbing both "gear and wheel support" pieces and add 7 bearings with a 6mm inner diameter and a 13mm outer diameter to each support. Make sure to leave one hole on the far side with the extention empty as that one wont hold a gear.

It should look like this:

<img width="589" height="81" alt="image" src="https://github.com/user-attachments/assets/d2372a57-cb13-4109-8b53-55b8f8a3c412" />

After that start adding your gears. Start by adding gear 1 to the first bearing from the side with the extention. Make sure to add the bearing to the flat side of the support, otherwise it will not fit.

<img width="447" height="250" alt="image" src="https://github.com/user-attachments/assets/80786f62-9313-4749-8b23-8321a8ae703e" />

After this add gear 2 to the bearing beside gear 1:

<img width="447" height="250" alt="image" src="https://github.com/user-attachments/assets/3340227a-1f83-4842-a369-4936a9d987f4" />

Then add gear 3 beside gear 2:

<img width="447" height="250" alt="image" src="https://github.com/user-attachments/assets/aa4e98b1-fdac-4570-80cd-a52140419d1b" />

Then add gear 4 beside gear 3:

<img width="447" height="250" alt="image" src="https://github.com/user-attachments/assets/5236c6f2-9ba6-4299-901b-21ec439f317b" />

Then add gear 5 beside gear 4:

<img width="432" height="186" alt="image" src="https://github.com/user-attachments/assets/fa48fac4-5f4d-4916-b255-7762e9e4198c" />

Then add gear A beside gear 5:

<img width="436" height="123" alt="image" src="https://github.com/user-attachments/assets/c43f767c-b962-4b60-8edd-f8c14ff4da79" />

Then add gear B beside gear A:

<img width="1152" height="2048" alt="image" src="https://github.com/user-attachments/assets/aa87b6ec-8554-4f73-814c-a082f3509ebc" />

Now repeat this exactly on the other support.

Next up, use Plastic glue to glue together barrel 1 and barrel 2. You can use glue here as these pieces never need to be seperated and are only seperate for easy of printing.

It should look roughly like this:

<img width="1014" height="368" alt="image" src="https://github.com/user-attachments/assets/0ef68fd7-b886-40d4-bf33-c46983b3529d" />

After this glue on the two gear and wheel support pieces making it so the side with the extention on the supports is on the wide side of the barrel with the lip. If that doesnt make sense i understand so ill show two angles of this step:

<img width="1021" height="525" alt="image" src="https://github.com/user-attachments/assets/b99c6ac5-ed01-4a2f-a7b9-9a84b70b59c5" />

<img width="753" height="574" alt="image" src="https://github.com/user-attachments/assets/d623d520-3222-45e3-bf59-11343ee00b65" />

Next grab Support piece 2 with the stock attached, and slide it through the bottom square hole of the barrel. No glue required as this part might need to be seperated for maintenence. For this step i will also add 2 angles:

<img width="886" height="562" alt="image" src="https://github.com/user-attachments/assets/76cf4572-82e9-4ac7-841b-97bda35067f0" />

<img width="829" height="384" alt="image" src="https://github.com/user-attachments/assets/509202bc-2196-4d35-a16f-306fe8a4683c" />

Then grab Support piece 1 and do the same as with support piece 2, exept this time on the top square hole and without the stock.

<img width="829" height="384" alt="image" src="https://github.com/user-attachments/assets/4b2e29d1-56fc-460d-8299-e5105578ed57" />

Following this add the PCB and Battery holder to the back of the barrel, glue is optional, you could add it if it falls off but if placed right it should fit nice and snug. For this i will again add two angles for clarity:

<img width="609" height="263" alt="image" src="https://github.com/user-attachments/assets/da99488b-5c25-4ee5-b1b4-18e80a28d418" />

<img width="834" height="433" alt="image" src="https://github.com/user-attachments/assets/0ae5caf9-7d63-4b37-a18d-4f3b59e8fd4f" />

The next step is adding the actual electronics. First take the pcb and add it to the pcb holder (i left my battery unconnected cause its more dificult to add the pcb to the holder with the battery attached):

it should look like this:

<img width="427" height="559" alt="image" src="https://github.com/user-attachments/assets/e272b88d-e995-4630-b8a9-6d45d26c87de" />

Next add the battery on top of the pcb holder. 

<img width="427" height="559" alt="image" src="https://github.com/user-attachments/assets/a17276e5-cb5f-44e8-a067-dc6528c3c990" />


 




















