path = cd;

Folderlist = {'06uA','07uA','08uA','09uA','10uA','11uA',...
    '12.0uA','12.2uA','12.4uA','12.6uA','12.8uA'};


for index = 1:length(Folderlist)
    filelist = dir([path,'/',Folderlist{index},'/']);
    length(filelist)
end

