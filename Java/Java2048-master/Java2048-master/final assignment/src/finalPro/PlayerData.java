package finalPro;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class PlayerData extends GameServer implements Runnable{
	public String name = null;
	public int[][] nums = new int[4][4];
	public int score = 0;
	private Socket socket;
	
	public PlayerData(Socket socket, String name) {
		this.socket = socket;
		this.name = name;
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		try {
    		DataInputStream input = new DataInputStream(socket.getInputStream());
    		DataOutputStream output = new DataOutputStream(socket.getOutputStream());
    		while(true) {
    			for(int i = 0; i < 4; i++) {
        			for(int j = 0; j < 4; j++) {
        				nums[i][j] = input.readInt();
       					remindTable.append("data received from client: " + nums[i][j] + '\n');
       				}
       			}
        		remindTable.append(this.name + " saved the game");
        		for(int i = 0; i < 4; i++) {
        			for(int j = 0; j < 4; j++) {
        				output.writeInt(nums[i][j]);
        			}
       			}
    			remindTable.append(this.name + " loaded the game");
    		}
    		
    	}
    	catch(IOException ex) {
    		ex.printStackTrace();
    	}
	}
}
