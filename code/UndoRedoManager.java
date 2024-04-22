import javax.swing.undo.UndoManager;

public class UndoRedoManager {
    private UndoManager undoManager;

    public UndoRedoManager() {
        undoManager = new UndoManager();
    }

    public void undo() {
        if (undoManager.canUndo()) {
            undoManager.undo();
        }
    }

    public void redo() {
        if (undoManager.canRedo()) {
            undoManager.redo();
        }
    }

    public void addEdit(javax.swing.undo.UndoableEdit edit) {
        undoManager.addEdit(edit);
    }
}
