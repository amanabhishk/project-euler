//STOP HERE

#include<stdio.h>
// #include<math.h>
using namespace std;

int main()
{
	int l;
	scanf("%d",&l);
	// l = 1;
	while (l>0)
	{
		l--;
		int i;
		int output[160] = {0};
		
		scanf("%d",&i);
		
		output[0] = i%10;
		output[1] = ((i-i%10)/10)%10;
		if (i==100) output[2] = 1;
		// i--;

		int p = 4;
		int index,temp;
		int carry;
		int number = 2;
		while (number<i)
		{
			index = 0;
			temp = 0, carry = 0;
			while (index<160)
			{
				temp = carry + output[index]*number;
				output[index] = temp%10;  
				carry = (temp-temp%10)/10;
				index++;
			}

			p=4;
			while (p>-1)
		{
			p--;
		}

			number++;
		}

		p = 159;
		
		// int t=p;
		while(p>-1 && output[p]==0)
		{
			p--;
		}
		
		

		while (p>-1)
		{
			printf("%d", output[p]);
			p--;
		}

		printf("\n");











		// int j = 0, len = 160;
		
		// int row,zeros;
		// while (i >1)
		// {
		// 	zeros = 0, row = 0;
		// 	int temp;
		// 	while (j < len)
		// 	{
				
		// 		temp = output[j]*i;
		// 		row = row + temp*pow(10,zeros);
		// 		zeros++;
		// 		j++;
		// 	} 
				
		// 	i--;
		// }



















	}
	


	return 0;
}