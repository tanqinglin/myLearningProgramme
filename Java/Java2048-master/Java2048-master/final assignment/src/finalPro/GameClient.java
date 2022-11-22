package finalPro;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.net.*;

public class GameClient {
	DataOutputStream toServer = null;
	DataInputStream fromServer = null;
	Socket socket = null;
	Frame2048 Game = new Frame2048();
	
	public GameClient() {
		ManageConnection();
	}
	
	private void ManageConnection() {
		//saving
		class SaveItemListener implements ActionListener {
	    	public void actionPerformed(ActionEvent e){
	    		try {
	    			toServer.writeInt(101);
	    			toServer.flush();
	    			for(int i = 0; i < 4; i++) {
			        	for(int j = 0; j < 4; j++) {
			        		toServer.writeInt(Game.G.numBuffers[i][j]);
			        	}
			        }
	    			toServer.writeInt(Game.G.GameScore);
	    			toServer.flush();
	    			System.out.println("Game saved successfully");
	    		}
	    		catch (IOException ex) {
	    			System.out.println("Data writing failed");
	    			ex.printStackTrace();
	    	    }
	    		
	    		
	    	}
	    }
		ActionListener Slistener = new SaveItemListener();
		
		//loading
		class LoadItemListener implements ActionListener {
	    	public void actionPerformed(ActionEvent e){
	    		try {
	    			toServer.writeInt(202);
	    			toServer.flush();
	    			for(int i = 0; i < 4; i++) {
	    	        	for(int j = 0; j < 4; j++) {
	    	        		Game.G.numBuffers[i][j] = fromServer.readInt();
	    	        	}
	    	        }
	    			Game.G.GameScore = fromServer.readInt();
	    			System.out.println("Game loaded successfully");
	    		}
	    		catch (IOException ex) {
	    			System.out.println("Data reading failed");
	    			ex.printStackTrace();
	    	    }
	    		
	    		Game.BlockVisible();
	    	}
	    }
		ActionListener Llistener = new LoadItemListener();
		
		//new player
		class NewPlayerListener implements ActionListener {
	    	public void actionPerformed(ActionEvent e){
	    		NameFrame getName = new NameFrame();
	    		getName.setVisible(true);
	    		class NameListener implements ActionListener {
					public void actionPerformed(ActionEvent e) {
						String temp = getName.textField.getText().trim();
						if(!temp.isEmpty()) {
							Game.Player = Integer.parseInt(temp);
							getName.dispose();
							try {
								//create socket when the name is typed					
				    			Game.SaveItem.addActionListener(Slistener);
				    			Game.LoadItem.addActionListener(Llistener);
				    			
				    			socket = new Socket("localhost", 8000);
				    			toServer = new DataOutputStream(socket.getOutputStream());
								fromServer = new DataInputStream(socket.getInputStream());
								
								toServer.writeInt(Game.Player);
								toServer.flush();
								
								Game.Player = fromServer.readInt();
								System.out.println("Player : " + Game.Player + " is playing the game!");
				    		}
				    		catch (IOException ex) {
				    			System.out.println("Create player failed");
				    			ex.printStackTrace();
				    	    }
						}
					}
	    		}
	    		ActionListener Nlistener = new NameListener();
	    	    getName.confirmName.addActionListener(Nlistener);
	    	    //already get the name
	    	    
	    	}
	    }
		ActionListener Plistener = new NewPlayerListener();
	    Game.NewPlayer.addActionListener(Plistener);
		
	}
	
	public static void main(String[] args) {
		GameClient GC = new GameClient();
		GC.Game.setVisible(true);
	}
	
}
