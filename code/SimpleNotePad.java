import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JColorChooser;
import javax.swing.JFileChooser;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class SimpleNotePad extends JFrame {
    private JTextArea textArea;
    private JFileChooser fileChooser;
    private String currentFile;

    public SimpleNotePad() {
        setTitle("Simple Notepad");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        textArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(textArea);
        add(scrollPane, BorderLayout.CENTER);

        JMenuBar menuBar = new JMenuBar();
        JMenu fileMenu = new JMenu("File");
        JMenuItem newMenuItem = new JMenuItem("New");
        JMenuItem openMenuItem = new JMenuItem("Open");
        JMenuItem saveMenuItem = new JMenuItem("Save");
        JMenuItem saveAsMenuItem = new JMenuItem("Save As");
        JMenuItem changeBgColorMenuItem = new JMenuItem("Change Background Color"); // New menu item
        fileMenu.add(newMenuItem);
        fileMenu.add(openMenuItem);
        fileMenu.add(saveMenuItem);
        fileMenu.add(saveAsMenuItem);
        fileMenu.add(changeBgColorMenuItem); // Add the new menu item
        menuBar.add(fileMenu);

        JMenu editMenu = new JMenu("Edit");
        JMenuItem undoMenuItem = new JMenuItem("Undo");
        JMenuItem redoMenuItem = new JMenuItem("Redo");
        JMenuItem cutMenuItem = new JMenuItem("Cut");
        JMenuItem copyMenuItem = new JMenuItem("Copy");
        JMenuItem pasteMenuItem = new JMenuItem("Paste");
        editMenu.add(undoMenuItem);
        editMenu.add(redoMenuItem);
        editMenu.add(cutMenuItem);
        editMenu.add(copyMenuItem);
        editMenu.add(pasteMenuItem);
        menuBar.add(editMenu);

        setJMenuBar(menuBar);

        fileChooser = new JFileChooser();
        ActionHandler actionHandler = new ActionHandler(textArea, fileChooser);

        newMenuItem.addActionListener(actionHandler);
        openMenuItem.addActionListener(actionHandler);
        saveMenuItem.addActionListener(actionHandler);
        saveAsMenuItem.addActionListener(actionHandler);
        changeBgColorMenuItem.addActionListener(new ActionListener() { // Add action listener for background color change
            public void actionPerformed(ActionEvent e) {
                changeBackgroundColor();
            }
        });

        setVisible(true);
    }

    // Method to change background color
    private void changeBackgroundColor() {
        Color bgColor = JColorChooser.showDialog(this, "Choose Background Color", textArea.getBackground());
        if (bgColor != null) {
            textArea.setBackground(bgColor);
            // Update background color for JMenuBar
            JMenuBar menuBar = getJMenuBar();
            if (menuBar != null) {
                menuBar.setBackground(bgColor);
            }
        }
    }

    public static void main(String[] args) {
        new SimpleNotePad();
    }
}
