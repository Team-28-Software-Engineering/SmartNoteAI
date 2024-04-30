import javax.swing.*;
import javax.swing.text.BadLocationException;
import javax.swing.text.DefaultHighlighter;
import javax.swing.text.Highlighter;
import javax.swing.undo.UndoManager;
import javax.swing.undo.UndoableEdit;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import javax.swing.event.UndoableEditEvent;
import javax.swing.event.UndoableEditListener;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class SimpleNotePad extends JFrame {
    private Highlighter.HighlightPainter highlightPainter = new DefaultHighlighter.DefaultHighlightPainter(Color.YELLOW);
    private JTextArea textArea;
    private JFileChooser fileChooser;
    private String currentFile;
    private Stack<UndoableEdit> undoStack;
    private Stack<UndoableEdit> redoStack;
    private int maxUndoRedoSteps = 10; // Limit undo and redo steps to 10
    
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
        JMenuItem findMenuItem = new JMenuItem("Find");


        // Thêm phím tắt cho các menu item
        newMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask()));
        openMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_O, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask()));
        saveMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask()));
        saveAsMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask() | KeyEvent.SHIFT_DOWN_MASK));
        findMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_F, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask()));
        

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
        fileMenu.add(findMenuItem);

        menuBar.add(fileMenu);

        JMenu editMenu = new JMenu("Edit");
        JMenuItem undoMenuItem = new JMenuItem("Undo");
        JMenuItem redoMenuItem = new JMenuItem("Redo");
        JMenuItem cutMenuItem = new JMenuItem("Cut");
        JMenuItem copyMenuItem = new JMenuItem("Copy");
        JMenuItem pasteMenuItem = new JMenuItem("Paste");
        undoMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Z, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask()));
        redoMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Y, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask()));
        cutMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_X, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask()));
        copyMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_C, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask()));
        pasteMenuItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_V, Toolkit.getDefaultToolkit().getMenuShortcutKeyMask()));

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
        // Enable undo and redo support
        undoStack = new Stack<>();
        redoStack = new Stack<>();
        textArea.getDocument().addUndoableEditListener(new UndoableEditListener() {
            @Override
            public void undoableEditHappened(UndoableEditEvent e) {
                if (undoStack.size() == maxUndoRedoSteps) {
                    undoStack.remove(0); // Remove the oldest edit if the stack is full
                }
                undoStack.push(e.getEdit());
                redoStack.clear(); // Clear redo stack on new edit
            }
        });        
        undoMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                undo();
            }
        });
        redoMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                redo();
            }
        });
        cutMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textArea.cut();
            }
        });
        
        copyMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textArea.copy();
            }
        });
        
        pasteMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textArea.paste();
            }
        });
        
        findMenuItem.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
                String searchText = JOptionPane.showInputDialog(SimpleNotePad.this, "Enter text to find:");
                if (searchText != null && !searchText.isEmpty()) {
                    highlightText(searchText);
                }
            }
        });
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
        textArea.getDocument().addDocumentListener(new DocumentListener() {
            @Override
            public void insertUpdate(DocumentEvent e) {
                removeAllHighlights();
            }
        
            @Override
            public void removeUpdate(DocumentEvent e) {
                removeAllHighlights();
            }
        
            @Override
            public void changedUpdate(DocumentEvent e) {
                // Do nothing
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
    
    
    // Phương thức để loại bỏ việc bôi vàng
    private void removeAllHighlights() {
        Highlighter highlighter = textArea.getHighlighter();
        highlighter.removeAllHighlights();
    }
    private void highlightText(String searchText) {
    Highlighter highlighter = textArea.getHighlighter();
    highlighter.removeAllHighlights(); // Xóa tất cả các nổi bật trước đó

    String text = textArea.getText();
    int index = text.indexOf(searchText);
    while (index >= 0) {
        try {
            highlighter.addHighlight(index, index + searchText.length(), highlightPainter);
            index = text.indexOf(searchText, index + 1);
        } catch (BadLocationException e) {
            e.printStackTrace();
        }
    }

    textArea.requestFocusInWindow(); // Đảm bảo JTextArea được focus để cuộn đến vị trí của văn bản nổi bật đầu tiên
    }
    private void undo() {
        if (!undoStack.isEmpty()) {
            UndoableEdit edit = undoStack.pop();
            edit.undo();
            redoStack.push(edit);
        }
    }

    private void redo() {
        if (!redoStack.isEmpty()) {
            UndoableEdit edit = redoStack.pop();
            edit.redo();
            undoStack.push(edit);
        }
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