
package datagram_send;

import java.net.*;
import java.io.*;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Datagram_send{
  public static void main(String[] args) throws IOException {
    DatagramSocket s = null;
    String salir = "";
    
      try {
          s = new DatagramSocket();
      } catch (SocketException ex) {
          Logger.getLogger(Datagram_send.class.getName()).log(Level.SEVERE, null, ex);
      }
    byte[] buf = new byte[1024];
    DatagramPacket dp = new DatagramPacket(buf, buf.length);

    InetAddress hostAddress = null;
      try {
          hostAddress = InetAddress.getByName("localhost");
      } catch (UnknownHostException ex) {
          Logger.getLogger(Datagram_send.class.getName()).log(Level.SEVERE, null, ex);
      }
    while (true) {
        String outMessage = "";
        BufferedReader stdin;
      do{
        stdin = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Que desea hacer?\n\t1. Jugar por concepto.\n\t2. Jugar por anagrama.\n\t3. Mostrar estadísticas.\n\t4. Salir del juego\n");
        outMessage = stdin.readLine();
      }while(!outMessage.matches("[1-4]{1}"));


      buf = outMessage.getBytes();

      DatagramPacket out = new DatagramPacket(buf, buf.length, hostAddress, 8000);
      s.send(out);
      if (outMessage.equals("4"))
        break;
      if(outMessage.equals("3")){
          s.receive(dp);
          int rows = Integer.parseInt(new String(dp.getData(), 0, dp.getLength()));
          int i = 0;
          String []datos = new String[rows];
          while (i<rows){
               s.receive(dp);
               String res = new String(dp.getData(), 0, dp.getLength());
               datos[i] = res;
               String []aux=datos[i].split("-");
               String []tiempo=aux[2].split(":");
               System.out.println("Tipo de juego: "+aux[0]+".\tDificultad: "+aux[1]+".\tTiempo: "+tiempo[0]+" horas, "+tiempo[1]+" minutos, "+tiempo[2]
               +" segundos.\tJugador: "+aux[3]+".\tPalabras: "+aux[43]);
              i++;
          }
          
      }
      else{
      s.receive(dp);
      String rcvd = "Servidor: "+ dp.getAddress() + ":" + dp.getPort() + "\nCantidad de palabras=" + new String(dp.getData(), 0, dp.getLength()) ;
         
      
      System.out.println(rcvd);
      int rows = Integer.parseInt(new String(dp.getData(), 0, dp.getLength()));
      int columns = 0;
      String []table = new String[rows+1];
      int i =0;
      while(i<rows){
        s.receive(dp);
        String rcvd2 = new String(dp.getData(), 0, dp.getLength());  
        int lr = rcvd2.length();
        columns = lr;
        String aux="";
        if (i==0){
           aux= "   ";
           for(int j=0;j<lr;j++){
               if(j<10)
                    aux+=j+"  ";
               else
                   aux+=j+" ";
           }//end for
           table[0]=aux;
           System.out.println(aux);
           aux="";
        }//end if
        
        for(int j=0;j<lr;j++){
            if(j==0){
                if(i<10)
                    aux+=i+"  ";
                else
                    aux+=i+" ";
            }//end if
            aux += rcvd2.charAt(j)+"  ";
        }//end for
        
        System.out.println(aux);
        i++;
        table[i]=aux;
      }// end while
     
      s.receive(dp);
      int wordsAmount = Integer.parseInt(new String(dp.getData(), 0, dp.getLength()));
      s.receive(dp);
      int tipo = Integer.parseInt(new String(dp.getData(), 0, dp.getLength()));
      s.receive(dp);
      String tema = new String(dp.getData(), 0, dp.getLength());
      System.out.println("El tema del crucigrama es:\n\t"+tema);
      if (tipo == 1){
          System.out.println("La dificultad del juego es: Facil");
          System.out.println("Se mostrará la lista de palabras por encontrar");
      }
      if (tipo == 2){
          System.out.println("La dificultad del juego es: Intermedia");
          System.out.println("Apareceran las palabras poco a poco conforme juegue");
      }//end if
      if (tipo == 3){
          System.out.println("La dificultad del juego es: Avanzada");
          System.out.println("Se mostrará la longitud de las palabras por encontrar");
      }//end if
      
      
      int res =0,k=0;
      do{
          if (k!=0)
              for(int j=0;j<table.length;j++)
                  System.out.println(table[j]);
          for(i=1;i<=wordsAmount;i++){
            s.receive(dp);       
                String rcvd2 = new String(dp.getData(), 0, dp.getLength());  
                System.out.println("\t"+i+". "+rcvd2);
    
          }// end for
           System.out.println("Para descubrir una palabra en el crucigrama debe ingresar su coordenada de inicio y de termino de la siguiente manera: x,y");
           String inicio="";
                   
           boolean val = false;
           int x1 = 0;
           int y1 = 0;
           
           do{
            System.out.println("Ingrese la coordenada de inicio: \n");
            inicio = stdin.readLine();
            if(!inicio.matches("[0-9]{1,3}[,][0-9]{1,3}"))
                System.out.println("No ingreso la coordenada con el formato adecuado, pruebe de nuevo");
            else{
                String []ini=  inicio.split(",") ;
                x1 = Integer.parseInt(ini[0]);
                y1 = Integer.parseInt(ini[1]);
                
                if(x1>=columns || x1<0){
                    val = true;
                    System.out.println("Ingreso la coordenada x fuera del rango, por favor ingrese una coordenada dentro del rango de (0,"+(columns-1)+")");
                }
                else if(y1>=rows || y1<0){
                    val = true;
                    System.out.println("Ingreso la coordenada y fuera del rango, por favor ingrese una coordenada dentro del rango de (0,"+(rows-1)+")");
                }
                else{
                    val = false;
                }
            }
           }
           while(!inicio.matches("[0-9]{1,3}[,][0-9]{1,3}") || val);
           String termino="";
           val = false;
           int x2 = 0;
           int y2 = 0;
           do{
            System.out.println("Ingrese la coordenada de termino: \n");
            termino = stdin.readLine();
            if(!termino.matches("[0-9]{1,3}[,][0-9]{1,3}"))
                System.out.println("No ingreso la coordenada con el formato adecuado, pruebe de nuevo");
            else{
                String []ini=termino.split(",") ;
                x2 = Integer.parseInt(ini[0]);
                y2 = Integer.parseInt(ini[1]);
                
                if(x2>=columns || x2<0){
                    val = true;
                    System.out.println("Ingreso la coordenada x fuera del rango, por favor ingrese una coordenada dentro del rango de (0,"+(columns-1)+")");
            }
            else if(y2>=rows || y2<0){
                val = true;
                System.out.println("Ingreso la coordenada y fuera del rango, por favor ingrese una coordenada dentro del rango de (0,"+(rows-1)+")");
            } 
            else if(x2==x1 && y2==y1 ){
                val = true;
                System.out.println("Ingrese una coordenada distinta a la coordenada de inicio");
            }
            else{
                val = false;
            }
          }
        }
           while(!termino.matches("[0-9]{1,3}[,][0-9]{1,3}") || val );
           
            buf =  String.valueOf(x1).getBytes();
            out = new DatagramPacket(buf, buf.length, hostAddress, 8000);
            s.send(out);
            
            buf =  String.valueOf(y1).getBytes();
            out = new DatagramPacket(buf, buf.length, hostAddress, 8000);
            s.send(out);
    
            buf =  String.valueOf(x2).getBytes();
            out = new DatagramPacket(buf, buf.length, hostAddress, 8000);
            s.send(out);
            
            buf =  String.valueOf(y2).getBytes();
            out = new DatagramPacket(buf, buf.length, hostAddress, 8000);
            s.send(out);
            
            s.receive(dp);
            
            res = Integer.parseInt(new String(dp.getData(), 0, dp.getLength()));  
            
            if(res==1 || res ==2){
                s.receive(dp);
                String res2 =new String(dp.getData(), 0, dp.getLength());
                System.out.println("Felicidades! Ha encontrado una palabra:");
                System.out.println(res2);
                if (res==2){
                    System.out.println("\n\n\tG\tA\tM\tE\t\tO\tV\tE\tR\n\n");
                    System.out.println("Su tiempo total fue:");
                    s.receive(dp);       
                    String tiempo = new String(dp.getData(), 0, dp.getLength()); 
                    String []t = tiempo.split(":");
                    System.out.println(t[0]+" horas.\t"+t[1]+" minutos.\t"+t[2]+" segundos.");
                    
                    boolean vn= false;
                    String nom = "";
                    do{
                       System.out.println("Ingrese su nombre sin acentos para el record:\n");
                       nom=stdin.readLine();
                       vn = nom.matches("[a-zA-Z]+");
                       if(!vn)
                           System.out.println("No ingreso el formato solicitado, pruebe de nuevo.");
                    }while(!vn);
                    buf = nom.getBytes();
                    out = new DatagramPacket(buf, buf.length, hostAddress, 8000);
                    s.send(out);
                }
            }else if(res==0){
                System.out.println("Lo sentimos. No encontro ninguna palabra.");
                s.receive(dp);
                String res2 =new String(dp.getData(), 0, dp.getLength());
                
            }
            boolean val2=false;

            if(res!=2)
                do{
                    System.out.println("Desea continuar? \n\t1. Si.\n\t2. No.");
                    salir = stdin.readLine();
                    val2 = salir.matches("[1-2]{1}");
                    if (!val2)
                        System.out.println("No ingreso un caracter valido.Pruebe de nuevo");
                }while(!val2);
            else
                salir="1";

                    
            buf =  salir.getBytes();
            out = new DatagramPacket(buf, buf.length, hostAddress, 8000);
            s.send(out);
            if(Integer.parseInt(salir)==2)
                break;
            k++;
        }
      while(res!=2);        
      }//end else
    } // end while
  } // end main
} // end class
