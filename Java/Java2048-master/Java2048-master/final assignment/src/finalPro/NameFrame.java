package finalPro;


import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class NameFrame extends JFrame{
	public JTextField textField = new JTextField(20);
	public JButton confirmName = new JButton("Confirm");
	public int a = 0;
	
	public NameFrame(){
		this.setSize(450,120);
		JLabel Tips = new JLabel("Please input your Player ID (Input 0 if you want to create a new Player)");
		JPanel AllPanel = new JPanel(new GridLayout(3,1));
		JPanel BPanel = new JPanel();
		BPanel.add(confirmName);
		AllPanel.setSize(120,60);
		AllPanel.add(Tips);
		AllPanel.add(textField);
		AllPanel.add(BPanel);
		this.add(AllPanel);
	}
}
