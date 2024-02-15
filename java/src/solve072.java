import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/*
 * 백준 10828 스택 
 * https://www.acmicpc.net/problem/10828
 * */

public class solve072 {
	private static int pointer = 0;
	
	public static void push(int[] customStack, int n) {
		
		customStack[pointer] = n;
		pointer += 1;
		
	}
	public static int pop(int[] customStack) {
		pointer -= 1;
		if (pointer >= 0) {
			return customStack[pointer];
		} else {
			pointer += 1;
			return -1;
		}
		
	}
	public static int size(int[] customStack) {
		return pointer;
	}
	public static int empty(int[] customStack) {
		if (pointer > 0) {
			return 0;
		} else {
			return 1;
		}
	}
	public static int top(int[] customStack) {
		if (pointer > 0) {
			return customStack[pointer - 1];
		} else {
			return -1;
		}
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int cmdCnt = Integer.parseInt(br.readLine());
		
		int[] customStack = new int[cmdCnt];
		
		
		for(int i = 0; i < cmdCnt ; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String cmd = st.nextToken();
			
			switch (cmd) {
				case "push" : push(customStack, Integer.parseInt(st.nextToken()));
					break;
				case "pop" : sb.append(pop(customStack) + "\n");

					break;
				case "size" : sb.append(size(customStack) + "\n");
					break;
				case "empty" : sb.append(empty(customStack) + "\n");
					break;
				case "top" : sb.append(top(customStack) + "\n");
					break;
			}
			
		}

		System.out.println(sb);
		
	}
}
