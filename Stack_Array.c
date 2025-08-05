#include<stdio.h>
#include<stdlib.h>
struct node 
{
    int size;
    int top;
    int *S;
};
void create(struct node *st,int x)
{
    // printf("Enter the size of the stack:- ");
    // scanf("%d",&st->size); 
    st->size = x;
    st->S = (int *)malloc(st->size * sizeof(int));
    st->top = -1;
}
void push(struct node *st , int x)
{
    if(st->top == st->size-1)
    printf("The stack is full");
    else
    {
        st->top++;
        st->S[st->top] = x;
    }
}
int pop(struct node *st)
{
    int x;
    x = st->S[st->top];
    st->top--;
    return x;
}
void display(struct node st)
{
    for(int i = st.top;i>=0;i--)
        printf("%d ",st.S[i]);
}
int main()
{
    struct node st;
    create(&st,5);
    push(&st,10);
    push(&st,20);
    push(&st,30);
    push(&st,40);
    push(&st,50);

    printf("The deleted element of the stack is %d\n",pop(&st));
    display(st);
    free(st.S);

// this is just endpoint
}
