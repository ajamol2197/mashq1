// 1
Console.Write("Yoshingizni kiriting: ");
int age = int.Parse(Console.ReadLine());
if (age >= 18) Console.WriteLine("Kattasiz");
else Console.WriteLine("Kichik");


// 2
Console.Write("1-sonni kiriting: ");
int a = int.Parse(Console.ReadLine());
Console.Write("2-sonni kiriting: ");
int b = int.Parse(Console.ReadLine());
if (a > b) Console.WriteLine("Birinchi son katta");
else Console.WriteLine("Ikkinchi son katta");


// 3
Console.Write("Son kiriting: ");
int n = int.Parse(Console.ReadLine());
if (n > 0) Console.WriteLine("Musbat son");
else Console.WriteLine("Manfiy son");


// 4
Console.Write("Raqam kiriting: ");
int r = int.Parse(Console.ReadLine());
if (r < 10) Console.WriteLine("10 dan kichik");
else if (r == 10) Console.WriteLine("10 ga teng");
else Console.WriteLine("10 dan katta");


// 5
Console.Write("1-son: ");
int s1 = int.Parse(Console.ReadLine());
Console.Write("2-son: ");
int s2 = int.Parse(Console.ReadLine());
if (s1 == s2) Console.WriteLine("Sonlar teng");
else Console.WriteLine("Sonlar teng emas");


// 6
Console.Write("So'z kiriting (hello/bye): ");
string txt = Console.ReadLine();
if (txt == "hello") Console.WriteLine("Salom!");
else if (txt == "bye") Console.WriteLine("Xayr!");
