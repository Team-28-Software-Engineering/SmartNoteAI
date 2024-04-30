import javax.swing.*;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

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

        // Disable line wrap
        textArea.setLineWrap(false);

        // Disable default Enter action (line break)
        Action enterAction = new AbstractAction() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textArea.insert("\n", textArea.getCaretPosition());
            }
        };
        textArea.getActionMap().put("enterAction", enterAction);
        textArea.getInputMap().put(KeyStroke.getKeyStroke(KeyEvent.VK_ENTER, 0), "enterAction");

        JMenuBar menuBar = new JMenuBar();
        JMenu fileMenu = new JMenu("File");
        JMenuItem newMenuItem = new JMenuItem("New");
        JMenuItem openMenuItem = new JMenuItem("Open");
        JMenuItem saveMenuItem = new JMenuItem("Save");
        JMenuItem saveAsMenuItem = new JMenuItem("Save As");
        JMenuItem changeBgColorMenuItem = new JMenuItem("Change Background Color");
        JMenuItem previewMenuItem = new JMenuItem("Preview File");
        JMenuItem tagFilesMenuItem = new JMenuItem("Tag Files"); // New menu item for tagging files
        JMenuItem exportHTMLMenuItem = new JMenuItem("Export as HTML");
        JMenuItem exportXMLMenuItem = new JMenuItem("Export as XML");
        JMenuItem exportJSONMenuItem = new JMenuItem("Export as JSON");

        fileMenu.add(newMenuItem);
        fileMenu.add(openMenuItem);
        fileMenu.add(saveMenuItem);
        fileMenu.add(saveAsMenuItem);
        fileMenu.add(changeBgColorMenuItem);
        fileMenu.add(previewMenuItem);
        fileMenu.add(tagFilesMenuItem);
        fileMenu.add(exportHTMLMenuItem); // Add export HTML menu item
        fileMenu.add(exportXMLMenuItem); // Add export XML menu item
        fileMenu.add(exportJSONMenuItem); // Add export JSON menu item

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
        changeBgColorMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                changeBackgroundColor();
            }
        });
        previewMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                previewFile();
            }
        });
        tagFilesMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                tagFiles();
            }
        });

        exportHTMLMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                exportAsHTML();
            }
        });

        exportXMLMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                exportAsXML();
            }
        });

        exportJSONMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                exportAsJSON();
            }
        });

        setVisible(true);
    }

    private void changeBackgroundColor() {
        Color bgColor = JColorChooser.showDialog(this, "Choose Background Color", textArea.getBackground());
        if (bgColor != null) {
            textArea.setBackground(bgColor);
            JMenuBar menuBar = getJMenuBar();
            if (menuBar != null) {
                menuBar.setBackground(bgColor);
            }
        }
    }

    private void previewFile() {
        int returnVal = fileChooser.showOpenDialog(this);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            File file = fileChooser.getSelectedFile();
            StringBuilder fileContent = new StringBuilder();
            try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
                String line;
                int lineCount = 0;
                while ((line = reader.readLine()) != null && lineCount < 10) {
                    fileContent.append(line).append("\n");
                    lineCount++;
                }
            } catch (IOException ex) {
                ex.printStackTrace();
            }
            JOptionPane.showMessageDialog(this, fileContent.toString(), "Preview", JOptionPane.PLAIN_MESSAGE);
        }
    }

    private void tagFiles() {
        String tag = JOptionPane.showInputDialog(this, "Enter tag:");
        if (tag != null && !tag.isEmpty()) {
            List<File> taggedFiles = findFilesWithTag(tag);
            if (taggedFiles.isEmpty()) {
                JOptionPane.showMessageDialog(this, "No files found with tag: " + tag, "Tag Files", JOptionPane.INFORMATION_MESSAGE);
            } else {
                StringBuilder message = new StringBuilder("Files with tag '" + tag + "':\n");
                for (File file : taggedFiles) {
                    message.append(file.getAbsolutePath()).append("\n");
                }
                JOptionPane.showMessageDialog(this, message.toString(), "Tag Files", JOptionPane.INFORMATION_MESSAGE);
            }
        }
    }

    private List<File> findFilesWithTag(String tag) {
        List<File> taggedFiles = new ArrayList<>();
        File[] files = fileChooser.getCurrentDirectory().listFiles();
        for (File file : files) {
            if (file.getName().contains(tag)) {
                taggedFiles.add(file);
            }
        }
        return taggedFiles;
    }

    private void exportAsHTML() {
        HTMLExporter.export(textArea);
    }
    
    private void exportAsXML() {
        XMLExporter.export(textArea);
    }
    private void exportAsJSON() {
        JSONExporter.export(textArea);
    }
    public static void main(String[] args) {
        new SimpleNotePad();
    }
}
