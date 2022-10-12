% [X,Y,Z] = ndgrid(1:size(cube,1), 1:size(cube,2), 1:size(cube,3));
% pointsize = 30;
% scatter3(X(:), Y(:), Z(:), pointsize, cube(:));

% RGB=[0,0,0],[0,0,1],[0,1,1],[0,1,0],[1,1,0],[1,0,0],[1,1,1]
segpos = [0:0.05:1]';
segneg = [1:-0.05:0]';
one = ones(21,1);
zero = zeros(21,1);

gap1 = [zero zero segpos];
gap2 = [zero segpos one];
gap3 = [zero one segneg];
gap4 = [segpos one zero];
gap4 = [one segneg zero];
gap5 = [one segpos segpos];

% Black to red color map.
Cmapping = [gap1;gap2;gap3;gap4]
