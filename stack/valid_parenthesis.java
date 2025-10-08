import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        if (s.charAt(0) == '(' && s.charAt(0) == '{' && s.charAt(0) == '[') {
            return false;
        } else {
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (c == '(' || c == '{' || c == '[') {
                    stack.push(c);
                    continue;
                }

                if (c == ')' || c == '}' || c == ']') {
                    if (stack.isEmpty()) return false;
                    char top = stack.pop();
                    if (top == '(' && c != ')') {
                        return false;
                    } else if (top == '[' && c != ']') {
                        return false;
                    } else if (top == '{' && c != '}') {
                        return false;
                    }
                }
            }
        }
        return stack.isEmpty();
    }
}
