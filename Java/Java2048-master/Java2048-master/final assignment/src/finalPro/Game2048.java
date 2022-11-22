package finalPro;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.util.Stack;

public class Game2048 {
	public int[][] numBuffers = new int[4][4];
	public Stack<int[][]> historyRecord = new Stack<int[][]>();
	public int GameScore = 0;
	public int count = 0;
	
	public Game2048() {
		
	}
	
	public void InitialGame() {
		//Clear numbers
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				numBuffers[i][j] = 0;
			}
		}
		//Clear history record
		if(!historyRecord.empty()) {
			historyRecord.clear();
		}
		historyRecord = new Stack<int[][]>();
		//Clear count and game score
		count = 0;
		GameScore = 0;
		refreshBlock(numBuffers, 16);
		refreshBlock(numBuffers, 15);
	}
	
	public void KeyLeft() {
		for(int i = 0; i < 4; i++) {
			numBuffers[i] = updateLine(numBuffers[i]);
			for(int j = 0; j < 4; j++) {
				if(numBuffers[i][j]==0) {
					count++;
				}
			}
		}
	}
	
	public void KeyUp() {
		int[] temp = new int[4];
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				temp[j] = numBuffers[j][i];
			}
			temp = updateLine(temp);
			for(int j = 0; j < 4; j++) {
				numBuffers[j][i] = temp[j];
				if(temp[j]==0) {
					count++;
				}
			}
		}
	}
	
	public void KeyRight() {
		int[] temp = new int[4];
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				temp[j] = numBuffers[i][3-j];
			}
			temp = updateLine(temp);
			for(int j = 0; j < 4; j++) {
				numBuffers[i][3-j] = temp[j];
				if(temp[j]==0) {
					count++;
				}
			}
		}
	}
	
	public void KeyDown() {
		int[] temp = new int[4];
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				temp[j] = numBuffers[3-j][i];
			}
			temp = updateLine(temp);
			for(int j = 0; j < 4; j++) {
				numBuffers[3-j][i] = temp[j];
				if(temp[j]==0) {
					count++;
				}
			}
		}
	}
	//update the value of each line after each operation
	public int[] updateLine(int Line[]) {
		int[] updated = new int[] {0,0,0,0};
		Queue<Integer> buffer = new LinkedList<Integer>();
		for(int i = 0; i < 4; i++) {
			if(Line[i] != 0) {
				buffer.offer(Line[i]);
			}
		}
		for(int i = 0; i < 4; i++) {
			if(buffer.peek() != null) {
				int temp = buffer.poll();
				if(buffer.peek() != null) {
					if(temp == buffer.peek()) {
						updated[i] = 2*temp;
						this.GameScore += updated[i];
						buffer.poll();
					}
					else {
						updated[i] = temp;
					}
				}
				else {
					updated[i] = temp;
				}
			}
			else {
				updated[i] = 0;
			}
		}
		return updated;
	}
	//listen if the block change after press key
	public void UpdateHR() {
		if((!historyRecord.empty() && BlockChange(historyRecord.peek(), numBuffers)) || historyRecord.empty()) {
			refreshBlock(numBuffers, count);
			count = 0;
			int[][] Buffer = new int[4][4];
			for(int i = 0; i < 4; i++) {
				for(int j = 0; j < 4; j++) {
					Buffer[i][j] = numBuffers[i][j];
				}
			}
			historyRecord.push(Buffer);
		}
	}
	
	//infer if the the block changes
	public boolean BlockChange(int Block1[][], int Block2[][]) {
		boolean t = false;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(Block1[i][j] != Block2[i][j]) {
					t = true;
				}
			}
		}
		return t;
	}
	//the function to refresh a new block of number
	public void refreshBlock(int Block[][], int count){
		Random random = new Random();
		int rand = random.nextInt(count)+1;
		int rand0 = random.nextInt(4)+1;
		if(rand0 != 4) {
			rand0 = 2;
		}
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(Block[i][j] == 0) {
					rand--;
					if(rand == 0) {
						Block[i][j] = rand0;
					}
				}
			}
		}
	}
	
}
