﻿using System;

namespace _04._Back_In_30_Minutes
{
    class Program
    {
        static void Main(string[] args)
        {
            int hours = int.Parse(Console.ReadLine());
            int mins = int.Parse(Console.ReadLine());

            mins += 30;

            if(mins > 59)
            {
                mins -= 60;
                hours += 1;
            }

            if(hours > 23)
            {
                hours = 0;
            }

            Console.WriteLine($"{hours}:{(mins < 10 ? "0" + mins : mins)}");
        }
    }
}