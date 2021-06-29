function [dsm] =  DSM( depthSequence )
%[dsm] = depthSequence{1};
depthSequence = depthSequence/255.0;
dsm = zeros(240, 320);
for i=1 : 240 % 240 rows
    for j=1 : 320 % 320 cols
        dsm(i,j) = depthSequence(i,j,1); 
    end
end
for k=2 : 40 %40 frames
    for i=1 : 240 % 240 rows
        for j=1 : 320 % 320 cols
            dsm(i,j)=max(dsm(i,j),depthSequence(i,j,k));
        end
    end
end
for k=1 : 40
    for i=1 : 240
        for j=1 : 320
            if(depthSequence(i,j,k)~=0)
                dsm(i,j)=min(dsm(i,j),depthSequence(i,j,k));
            end
        end
    end
end
end