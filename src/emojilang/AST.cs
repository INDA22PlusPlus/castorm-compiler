using System.Generic.Collections;

public class AST 
{
    public ASTNode Root { get; }
    public AST(ASTNode root) 
    {
        Root = root;
    }
}

public class ASTNode 
{
    public List<ASTNode> Children { get; }
    public NodeType NodeType { get; }
    public ASTNode(NodeType type, IEnumerable<ASTNode> children) 
    {
        NodeType = type;
        Children = new List<ASTNode>(children);
    }

    public abstract int Execute();
}

public enum NodeType 
{
    OUTPUT,
    ADDITION, 
    SUBTRACTION, 
    MULTIPLICATION, 
    DIVISION, 
    WHILE, 
    IF, 
    ASSIGNMENT, 
    VALUE, 
    // IDENTIFIER????
}