/* 
 * Client service Daytime
 * see RFC 867 - http://tools.ietf.org/html/rfc867
 *
 */
 
import java.io.*;
import java.net.*;

public class ClientDaytime extends Object {
  public static void main (String args[]) {
    String          reponse;
    Socket          leSocket;
    // PrintStream     fluxSortieSocket; inutile dans ce cas ...
    BufferedReader  fluxEntreeSocket;

    try {
      // creation d’une socket et connexion à la machine localhost sur le port numéro 13
      leSocket = new Socket("localhost", 13); // remplacer le nom de machine si nécessaire !
      System.out.println("Connecté sur : "+leSocket);

      // Création d’un flux de type BufferedReader lié au flux d’entrée de la socket
      fluxEntreeSocket = new BufferedReader(new InputStreamReader(leSocket.getInputStream()));
      // Le flux de sortie est inutile pour ce service ! La connexion vaut requête !!!
      
      // attente puis réception de données envoyées par le serveur
      reponse = fluxEntreeSocket.readLine(); // lit dans la socket jusqu'à trouver un "\n" (nouvelle ligne)
      System.out.println("Reponse du serveur daytime : " + reponse);

      leSocket.close(); // fermer la socket
      
    } // end try
    catch (UnknownHostException ex) {
      System.err.println("La machine est inconnue : "+ex);
      ex.printStackTrace();
    }
    catch (IOException ex) {
      System.err.println("Autre type d'eErreur : "+ex);
      ex.printStackTrace();
    }
  } // main
} // end class
