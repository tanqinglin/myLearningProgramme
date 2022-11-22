package finalPro;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Random;
import java.util.Stack;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.RootPaneContainer;


public class Frame2048 extends JFrame{
	
	public ImagePanel[][] numImages = new ImagePanel[4][4];
	public Map<Integer,String> numPath = new HashMap<Integer,String>();
	public Game2048 G = new Game2048();
	public JPanel GamePad = new JPanel();
	public JLabel ScoreBox = new JLabel();
	public JMenuItem NewPlayer = new JMenuItem("New Player");
	public JMenuItem SaveItem = new JMenuItem("Save");
	public JMenuItem LoadItem = new JMenuItem("Load");
	public int Player = 0;
	
	public Frame2048() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setBackground(Color.WHITE);

		//add Path
		numPath.put(0, "src/finalPro/2048/0.png");
		numPath.put(2, "src/finalPro/2048/2.png");
		numPath.put(4, "src/finalPro/2048/4.png");
		numPath.put(8, "src/finalPro/2048/8.png");
		numPath.put(16, "src/finalPro/2048/16.png");
		numPath.put(32, "src/finalPro/2048/32.png");
		numPath.put(64, "src/finalPro/2048/64.png");
		numPath.put(128, "src/finalPro/2048/128.png");
		numPath.put(256, "src/finalPro/2048/256.png");
		numPath.put(512, "src/finalPro/2048/512.png");
		numPath.put(1024, "src/finalPro/2048/1024.png");
		numPath.put(2048, "src/finalPro/2048/2048.png");
		
		//set frame and game panel
		this.setSize(400, 500);
		
		Dimension size = new Dimension(375, 375);
		GamePad.setPreferredSize(size);
		GamePad.setLayout(new GridLayout(4,4,5,5));
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				numImages[i][j] = new ImagePanel(numPath.get(0));
				GamePad.add(numImages[i][j]);
			}
		}
		
		JLabel Title = new JLabel("  2048!");
		Title.setFont(new Font("", Font.BOLD, 30));
		JPanel InfoPad = new JPanel();
		InfoPad.setLayout(new BorderLayout());
		ScoreBox.setText("Score: " + G.GameScore);
		ScoreBox.setFont(new Font("", Font.BOLD, 20));
		InfoPad.add(Title, BorderLayout.WEST);
		InfoPad.add(ScoreBox, BorderLayout.EAST);
		
		JPanel outsider1 = new JPanel();
		outsider1.setSize(375,375);
		outsider1.add(GamePad);
		
		JPanel AllPad = new JPanel(new BorderLayout());
		AllPad.add(outsider1, BorderLayout.SOUTH);
		AllPad.add(InfoPad, BorderLayout.CENTER);
		this.add(AllPad);
		//set menu
		JMenu MenuB = new JMenu("Menu");
		createMenus(MenuB);
		JMenuBar MenuBar = new JMenuBar(); 
	    MenuBar.add(MenuB);
	    this.setJMenuBar(MenuBar);
	    
	    this.setTitle("Game 2048");
	}
	
	//add key listener to listen the direction key
	public KeyListener KL = new KeyListener() {

		@Override
		public void keyTyped(KeyEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void keyPressed(KeyEvent e) {
			// TODO Auto-generated method stub
			if(e.getKeyCode() == 37) {
				//System.out.println("按了左");
				G.KeyLeft();
			}
			else if(e.getKeyCode() == 38) {
				//System.out.println("按了上");
				G.KeyUp();
			}
			else if(e.getKeyCode() == 39) {
				//System.out.println("按了右");
				G.KeyRight();
			}
			else if(e.getKeyCode() == 40) {
				//System.out.println("按了下");
				G.KeyDown();
			}
			
			G.UpdateHR();
			BlockVisible();
			//System.out.println(Player);
		}

		@Override
		public void keyReleased(KeyEvent e) {
			// TODO Auto-generated method stub
			
		}
	};
	//refresh the outlook
	public void BlockVisible() {
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				numImages[i][j].img = new ImageIcon(numPath.get(G.numBuffers[i][j])).getImage();
				numImages[i][j].repaint();
				//System.out.println(numBuffers[i][j]);
			}
		}
		ScoreBox.setText("Score: " + G.GameScore);
	}
	
	private void createMenus(JMenu MenuFile) {
		/* add a "File" menu with:
		 * "Open" item which allows you to choose a new file
		 * "Exit" item which ends the process with System.exit(0);
		 * Key shortcuts are optional
		 */
		JMenuItem NewGame = new JMenuItem("New Game");
		JMenuItem ExitItem = new JMenuItem("Exit");
	    class ExitItemListener implements ActionListener {
	    	public void actionPerformed(ActionEvent e){
	            System.exit(0);
	    	}
	    }
		ActionListener Elistener = new ExitItemListener();
	    ExitItem.addActionListener(Elistener);
	    
	    //initial a new game
	    class NewGameListener implements ActionListener {
	    	public void actionPerformed(ActionEvent e){
	    		if(Player != 0) {
	    			StartGame();
	    		}
	    	}
	    }
		ActionListener Glistener = new NewGameListener();
	    NewGame.addActionListener(Glistener);
	    
	    //create new player
	    
	    
	    MenuFile.add(NewGame);
	    MenuFile.add(NewPlayer);
		MenuFile.add(SaveItem);
		MenuFile.add(LoadItem);
		MenuFile.add(ExitItem);
			
	}
	
	public void StartGame() {
		G.InitialGame();
		BlockVisible();
		//add listener
		this.addKeyListener(KL);
		ScoreBox.setText("Score: " + 0);
	}
	
	public static void main(String[] args) {
		Frame2048 Game = new Frame2048();
		Game.setVisible(true);
		//Game.StartGame();
		//Game.G.numBuffers = new int[][] {{32,32,4,4},{32,0,2,0},{2,2,2,2},{2,0,0,4}};
	}
}
