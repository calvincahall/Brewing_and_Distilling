function out = testfun1(A)

a1=A;

b=find(a1<1)' % eliminate negative integers
a1(b)=[];
a=a1;
c=sort(a); % sort in ascending order

t=[1:(max(A)+1)];


index=[];
for i=1:(length(c)-1) % find duplicates
    if c(i)==c(i+1)
        index(i)=i;
    end
end

% eliminate duplicates
d=find(index);
c(d)=[];

clear index a b

for i=1:length(t)
    a=c==t(i);
    b=find(a);
    if isempty(b)==1
        index=i;
        break
    end

end

out=t(index);

end
