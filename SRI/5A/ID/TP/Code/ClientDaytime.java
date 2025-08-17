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
      // creation d�une socket et connexion � la machine localhost sur le port num�ro 13
      leSocket = new Socket("localhost", 13); // remplacer le nom de machine si n�cessaire !
      System.out.println("Connect� sur : "+leSocket);

      // Cr�ation d�un flux de type BufferedReader li� au flux d�entr�e de la socket
      fluxEntreeSocket = new BufferedReader(new InputStreamReader(leSocket.getInputStream()));
      // Le flux de sortie est inutile pour ce service ! La connexion vaut requ�te !!!
      
      // attente puis r�ception de donn�es envoy�es par le serveur
      reponse = fluxEntreeSocket.readLine(); // lit dans la socket jusqu'� trouver un "\n" (nouvelle ligne)
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
