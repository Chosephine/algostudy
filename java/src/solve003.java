import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 분수의 덧셈
*/

public class solve003{
	// 유클리드 호제법을 활용한 최대공약수 찾기 (n1 > n2)
	public static int gdc(int n1, int n2) {
		int a = n1;
		int b = n2;
		int r = a % b;
		while (r != 0) {
			a = b;
			b = r;
			r = a % b;
		}
		return b;
	}
	
    public static int[] solution(int numer1, int denom1, int numer2, int denom2) {
        
        
        // 덧셈 진행
        int denom = denom1 * denom2;
        int numer = numer1 * denom2 + numer2 * denom1;
        
        // 분자, 분모의 최대공약수 찾기
        int gdc = gdc(Math.max(numer, denom), Math.min(numer,  denom));
        
        // 정답 작성
        int[] answer = new int[]{numer / gdc, denom / gdc};
        
        return answer;
    }
    
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int[] answer = solution(1, 2, 3, 4);
    	System.out.printf(Arrays.toString(answer));
    	
    }
}
