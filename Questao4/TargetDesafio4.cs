using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    public static void Main()
    {
        Dictionary<string, double> faturamento = new Dictionary<string, double>();
        faturamento.Add("SP", 67836.43);
        faturamento.Add("RJ", 36678.66);
        faturamento.Add("MG", 29229.88);
        faturamento.Add("ES", 27165.48);
        faturamento.Add("Outros", 19849.53);
        
        double total = faturamento.Sum(x => x.Value);
        
        Console.WriteLine("Representação de cada Estado:");
        
        foreach (KeyValuePair<string, double> valor in faturamento) {
            Console.WriteLine("{0}: {1}%", valor.Key, (100 * valor.Value/total).ToString("0.00"));
        }
        
    }
}