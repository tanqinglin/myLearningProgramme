package finalPro;

import java.io.*;
import java.net.*;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Set;

import javax.swing.*;

public class GameServer extends JFrame implements Runnable {
	public JTextArea remindTable;
	public Map<Integer, Socket> Plist = new HashMap<Integer, Socket>();
	public GameServer() {
		remindTable = new JTextArea(10,10);
		JScrollPane sp = new JScrollPane(remindTable);
		this.add(sp);
		this.setTitle("TheGameServer");
		this.setSize(400,200);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Thread t = new Thread(this);
		t.start();
	}
	
	public void run() {
		try {
			ServerSocket serverSocket = new ServerSocket(8000);
			remindTable.append("Game Server started !" + '\n');
			int revname = 0;
			while (true) {
				Socket socket = serverSocket.accept();
				//wait for the player name
				DataInputStream input = new DataInputStream(socket.getInputStream());
				DataOutputStream output = new DataOutputStream(socket.getOutputStream());
				revname = input.readInt();
				if(revname == 0/*!Plist.containsKey(socket)*/) {
					int name = 0;
					Random random = new Random();
					name = random.nextInt(1000000)+1;
					while(Plist.containsKey(name)) {
						random = new Random();
						name = random.nextInt(1000000)+1;
					}
			    	Plist.put(name,socket);
			    	output.writeInt(name);
			    	output.flush();
			    	Player P = new Player(socket,name);
			    	
			    	//I just don't know why this thread always run twice
			    	if(P.start = false) {
			    		Thread t = new Thread(P);
			    		t.start();
			    		try {
							t.join();
						} catch (InterruptedException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
			    		P.start = true;
			    	}
				}
				remindTable.append("A new player connected" + '\n');
				System.out.println(Plist);
				
			}
		}
		catch(IOException e) {
			System.out.println("Server failed to run");
			e.printStackTrace();
		}
	}
	
	class Player extends GameServer implements Runnable{
		public int name = 0;
		public int[][] nums = new int[4][4];
		public int score = 0;
		public boolean start = false;
		private Socket socket;
		
		public Player(Socket socket, int name) {
			this.socket = socket;
			this.name = name;
			for(int i = 0; i < 4; i++) {
    			for(int j = 0; j < 4; j++) {
    				nums[i][j] = 0;
    			}
   			}
		}

		@Override
		public void run() {
			// TODO Auto-generated method stub
			try {
	    		DataInputStream input = new DataInputStream(socket.getInputStream());
	    		DataOutputStream output = new DataOutputStream(socket.getOutputStream());
	    		int opt = 0;
	    		while(true) {
	    			if(input.available() != 0) {
	    				//opt used to indicate the command
	    				opt = input.readInt();
	    				if(opt==101) {
	    					for(int i = 0; i < 4; i++) {
			        			for(int j = 0; j < 4; j++) {
			        				nums[i][j] = input.readInt();
			        				System.out.println("data received from client: " + nums[i][j] + '\n');
			       					remindTable.append("data received from client: " + nums[i][j] + '\n');
			       				}
			       			}
	    					score = input.readInt();
		    				remindTable.append(this.name + " saved the game");
		    				opt = 0;
	    				}
		        		if(opt==202) {
		        			for(int i = 0; i < 4; i++) {
			        			for(int j = 0; j < 4; j++) {
			        				output.writeInt(nums[i][j]);
			        			}
			       			}
		        			output.writeInt(score);
		        			output.flush();
			    			remindTable.append(this.name + " loaded the game");
			    			opt = 0;
		        		}
	    			}
	    		}
	    		
	    	}
	    	catch(IOException ex) {
	    		ex.printStackTrace();
	    	}
		}
	}

	public static void main(String[] args) {
		GameServer GS = new GameServer();
		GS.setVisible(true);
	}
}