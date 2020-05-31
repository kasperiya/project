using System;
using System.Threading;
namespace ConsoleApp1
{
    public class Program
    {
        static void Main(string[] args)
        {
            Customer customer = new Customer() { Bakiye = 2500, no_login = 0, password = 1453, Firstname = "havva" };

            Console.WriteLine("hoşgeldiniz");

            while (true)
            {
                Console.WriteLine("şifrenizi giriniz");
                var password = Convert.ToInt32(Console.ReadLine());


                if (password == customer.password)
                {
                Menu:
                    Console.WriteLine("hoşgeldizniz::{0}", customer.Firstname);
                    Console.WriteLine("para çekmek--1\n  para yatırmak için--2\n şifre degiştrimek için--3\n bakiye görüntülemek için--4\n çıkış için --5");
                    Console.WriteLine("tercihiniz nedir ");
                    var tercih = Convert.ToInt32(Console.ReadLine());
                    if (tercih == 1)
                    {
                        Console.WriteLine("istenilen miktar");
                        var miktar = Convert.ToInt32(Console.ReadLine());
                        if (miktar <= 0)
                        {
                            Console.WriteLine("geçersiz işlem işlemler anasayfasına yönlendiririliyorsunuz");
                            goto Menu;
                        }
                        else if (miktar > 0)
                        {
                            Topla(miktar);
                            Console.WriteLine("başka işlem yapmak istiyor musun e veya h yaz");
                            var option = Console.ReadLine();
                            if (option == "e" || option == "E")
                            {
                                Console.WriteLine("İŞLEMLER ANASAYFASINA YÖNLENDİRİRİLİYORSUNZ");
                                Thread.Sleep(2000);
                                goto Menu;
                            }
                            else if (option == "h" || option == "H")
                            {
                                Console.WriteLine("sistem kapatılıyor-----");
                                Thread.Sleep(2000);
                                Environment.Exit(0);
                            }
                        }

                    }
                    else if (tercih == 2)
                    {
                        Console.WriteLine("ne kadar yatıracaksın");
                        var amount = Convert.ToInt32(Console.ReadLine());
                        if (amount > 0)
                        {
                            Yatir(amount);
                            Console.WriteLine("başka işlem yapmak istiyor musun e veya h yaz");
                            var option = Console.ReadLine();
                            if (option == "e" || option == "E")
                            {
                                Console.WriteLine("İŞLEMLER ANASAYFASINA YÖNLENDİRİRİLİYORSUNZ");
                                Thread.Sleep(2000);
                                goto Menu;
                            }
                            else if (option == "h" || option == "H")
                            {
                                Console.WriteLine("sistem kapatılıyor-----");
                                Thread.Sleep(2000);
                                Environment.Exit(0);
                            }
                        }

                        if (amount < 0)
                        {
                            Console.WriteLine("geçersiz işlem");
                            Console.WriteLine("başka işlem yapmak istiyor musun e veya h yaz");
                            var option = Console.ReadLine();
                            if (option == "e" || option == "E")
                            {
                                Console.WriteLine("İŞLEMLER ANASAYFASINA YÖNLENDİRİRİLİYORSUNZ");
                                Thread.Sleep(2000);
                                goto Menu;
                            }
                            else if (option == "h" || option == "H")
                            {
                                Console.WriteLine("sistem kapatılıyor-----");
                                Thread.Sleep(2000);
                                Environment.Exit(0);
                            }

                        }
                    }
                    else if (tercih == 3)
                    {
                        while (true)
                        {
                            Console.WriteLine(" mevcut şifreniz");
                            var replace_paswrd = Convert.ToInt32(Console.ReadLine());
                            if (replace_paswrd == customer.password)
                            {
                                Console.WriteLine("şifre dogru");
                                Console.WriteLine("yeni şifreniz::");
                                var n_password = Convert.ToInt32(Console.ReadLine());
                                customer.password = n_password;
                                Console.WriteLine("şifreniz degişti işlemler anasayfasına yönlendiririliyorsunuz");
                                Thread.Sleep(2000);
                                goto Menu;

                            }
                            else if (replace_paswrd != customer.password)
                            {
                                customer.no_login += 1;
                                Console.WriteLine("şifre hatalı,yanlış girirlme sayısı::{0}", customer.no_login);
                            }
                            if (customer.no_login == 3)
                            {
                                Console.WriteLine("3 kez yanlış girdin kart bloke dediliyor");
                                Thread.Sleep(2000);
                                Environment.Exit(0);
                            }
                        }
                    }
                    else if (tercih == 4)
                    {
                        Console.WriteLine("bakiyeniz::{0}", customer.Bakiye);

                    }
                    else if (tercih == 5)
                    {
                        Console.WriteLine("sistem kapatılıyor...");
                        Thread.Sleep(2000);
                        Environment.Exit(0);
                    }

                    else if (password != customer.password)
                    {

                        customer.no_login += 1;
                        Console.WriteLine("şifre hatalı yanlış yanlış girirlme sayısı::{0} ", customer.no_login);
                        if (customer.no_login == 3)
                        {
                            Console.WriteLine("3 kez yanlış girildi sistem kapanıyır.....");
                            Thread.Sleep(2000);

                            Environment.Exit(0);

                        }

                    }






                }


                int Topla(int miktar)
                {
                    if (miktar > customer.Bakiye)
                    {
                        Console.WriteLine("yeetrsiz bakiye bakiyeniz::{0} ,istenilen miktar::{1}", customer.Bakiye, miktar);
                    }
                    else if (miktar <= customer.Bakiye)
                    {
                        customer.Bakiye -= miktar;
                        Console.WriteLine("yeni bakiyeniz::{0} istenilen miktar::{1}", customer.Bakiye, miktar);
                    }

                    return 0;
                }
                int Yatir(int miktar)
                {

                    customer.Bakiye += miktar;
                    Console.WriteLine("yatırırlan::{0} bakiye::{1}", miktar, customer.Bakiye);



                    return 0;

                }


            }

        }








        internal interface IAtm
        {

            int Bakiye { get; set; }
            int no_login { get; set; }
            int password { get; set; }
            string Firstname { get; set; }

        }
        public class Customer : IAtm
        {

            public int Bakiye { get; set; }
            public int no_login { get; set; }
            public int password { get; set; }
            public string Firstname { get; set; }
        }



    }
}










