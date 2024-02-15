import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/*
 * 백준 10828 스택 
 * https://www.acmicpc.net/problem/10828
 * */

public class solve072 {
	private static ArrayList<Integer> customStack = new ArrayList<Integer>();
	private static int pointer = 0;
	
	public static void push(int n) {
		try {
			customStack.get(pointer);
			customStack.set(pointer, n);
			pointer += 1;
		} catch (Exception IndexOutOfBoundsException) {
			customStack.add(n);
			pointer += 1;

		}
		
	}
	public static int pop() {
		pointer -= 1;
		if (pointer >= 0) {
			return customStack.get(pointer);
		} else {
			pointer += 1;
			return -1;
		}
		
	}
	public static int size() {
		return pointer;
	}
	public static int empty() {
		if (pointer > 0) {
			return 0;
		} else {
			return 1;
		}
	}
	public static int top() {
		if (pointer > 0) {
			return customStack.get(pointer - 1);
		} else {
			return -1;
		}
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int cmdCnt = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < cmdCnt ; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String cmd = st.nextToken();
			
			switch (cmd) {
				case "push" : push(Integer.parseInt(st.nextToken()));
					break;
				case "pop" : sb.append(pop() + "\n");
					break;
				case "size" : sb.append(size() + "\n");
					break;
				case "empty" : sb.append(empty() + "\n");
					break;
				case "top" : sb.append(top() + "\n");
					break;
			}
			
		}

		System.out.println(sb);
		
	}
}
