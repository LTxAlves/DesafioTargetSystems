using System;

public class Program
{
    public static void Main()
    {
        string entrada = Console.ReadLine();
        string saida = String.Empty;
        
        for (int i = entrada.Length - 1; i >= 0; i--) {
            saida += entrada[i];
        }
        
        Console.WriteLine(saida);
    }
}