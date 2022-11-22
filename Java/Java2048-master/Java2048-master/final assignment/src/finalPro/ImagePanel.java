package finalPro;

import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Random;

import javax.swing.ImageIcon;
import javax.swing.JPanel;

public class ImagePanel extends JPanel {
	public Image img;
	private int num = 1;
	
	public ImagePanel(String img) {
		this(new ImageIcon(img).getImage());
		//Image d1 = new ImageIcon("src/finalPro/2048/0.png").getImage();
		//this.img = d1;
		
	}
	public ImagePanel(Image img) {
		this.img = img;
        Dimension size = new Dimension(img.getWidth(null), img.getHeight(null));
        setPreferredSize(size);
        /*setMinimumSize(size);
        setMaximumSize(size);
        setSize(size);*/
        setLayout(null);
	}
	public int getnum() {
		return this.num;
	}
    public void paintComponent(Graphics g) {
        g.drawImage(img, 0, 0, null);
    }
}
