

/*
 * programmers 코딩테스트 입문
 * 옷가게 할인 받기
*/

public class solve012{
	
	public static int solution(int price) {
        double answer = price;
//        if (100000 <= price && price < 300000) {
//        	answer = price * 0.95;
//        } else if (300000 <= price && price < 500000){
//        	answer = price * 0.9;
//        } else {
//        	answer = price * 0.8;
        	// 이 경우 price < 100000 인 경우 및 price > 500000 인 경우 모두 20% 할인이 들어감
//        }
        if (price >= 500000) {
        	answer = price * 0.8;
        } else if (price >= 300000){
        	answer = price * 0.9;
        } else if (price >= 100000){
        	answer = price * 0.95;
        }
        
        return (int) Math.floor(answer);
    }

    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int price = 580000;
//    	int people = 12;
    	int answer = solution(price);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    }
}
