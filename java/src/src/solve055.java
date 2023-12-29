package src;

import java.util.Scanner;

/*
 * 백준 10950  A+B - 3
 * 입출력 연습
 * 백준 채점 시 클래스명은 Main이어야한다.
*/

public class solve055 {
	
	public static void main(String[] args)  throws Exception{
		
		/*
		 * Scanner 클래스는 공백과 개행(' ', '\t', '\r', '\n' 등) 을 기준으로 입력받음
		 * String이면 sc.nextLine(), int면 nextInt() 이런식!
		*/
		
		Scanner sc = new Scanner(System.in);
        
		int N = sc.nextInt();
		 
		for(int i = 0 ; i < N ; i++) {
			
			int A = sc.nextInt();
			int B = sc.nextInt();
			
			System.out.println(A + B);
		}
	
	}
	
	
}
