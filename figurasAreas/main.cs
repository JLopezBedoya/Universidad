using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Calcular el Area De un Circulo/Rectangulo");
        string opcion, temp, tempbase, tempalt, figura="f";
        char op;
        decimal comp, rad, alt, bas, total=0, pi = 3.14m;
        
        while(true){
            do{
                Console.WriteLine("Desea Conseguir el Area de un:");
                Console.WriteLine("1.Circulo");
                Console.WriteLine("2.rectangulo");
                opcion = Console.ReadLine();
                if (opcion.Length !=1){
                Console.WriteLine("Por Favor escriba 1 para elegir el circulo y el 2 para elegir el rectangulo");}
            }while (opcion.Length !=1);
            
            op = Convert.ToChar(opcion);
            
            switch (op){
                case '1':
                
                    Console.Write("Ingrese el Radio del Circulo: ");
                    temp = Console.ReadLine();
                    if (decimal.TryParse(temp, out comp)){
                        rad = Convert.ToDecimal(temp);
                        total = pi*(rad*rad);
                        figura = "Circulo";
                    }
                    else{
                        Console.WriteLine("El Radio Debe Ser un Numero");
                        continue;
                    }
                    break;
                    
                case '2':
                    Console.Write("Ingrese la base del Cuadrado: ");
                    tempbase = Console.ReadLine();
                    Console.Write("Ingrese la altura del Cuadrado: ");
                    tempalt = Console.ReadLine();
                    if (decimal.TryParse(tempbase, out comp) && decimal.TryParse(tempalt, out comp)){
                        alt = Convert.ToDecimal(tempalt);
                        bas = Convert.ToDecimal(tempbase);
                        total = bas*alt;
                        figura = "Rectangulo";
                    }
                    else{
                        Console.WriteLine("La Base y la Altura Deben Ser un Numero");
                        continue;
                    }
                    break;
                default:
                    Console.WriteLine("Por Favor escriba 1 para elegir el circulo y el 2 para elegir el rectangulo");
                    continue;
                    break;
            }
            Console.Write($"El Area del {figura} es de {total}, Presione Enter Para Continuar");
            Console.ReadLine();
    }
}
}
