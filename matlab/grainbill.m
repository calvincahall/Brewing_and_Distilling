function [output,varargout]=grainbill(tot,vol,varargin)

counter=1;
default=struct('pilsnermalt',0,'darkmunichmalt15l',0,'viennamalt',0,...
    'flakedbarley',0,'tworowmalt',0,'caramelmalt10l',0,'caramelmalt20l',0,...
    'caramelmalt30l',0,'caramelmalt40l',0,'caramelmalt60l',0,'caramelmalt80l',0,...
    'caramelmalt120l',0,'flakedwheat',0,'torrifiedwheat',0,'whitewheatmalt',0,...
    'biscuitmalt',0,'victorymalt',0,'abbeymalt',0,'palemalt',0,'chocolatemalt',0,...
    'blackpatentmalt',0,'carafaiiimalt',0,'ryemalt',0,'roastedbarleymalt',0,...
    'simpsongoldenpromisemalt',0,'englishpalemalt',0,'sixrowmalt',0,...
    'chocolatewheatmalt',0,'flakedoats',0,'redwheat',0,'rawwheat',0,...
    'carapils',0,'brownmalt',0,'blackmalt',0,'flakedcorn',0,'acidulatemalt',0,...
    'potstillmalt',0,'goldenpromise',0,'munichmalt',0,'ottermalt',0,...
    'cararubymalt',0,'carawheatmalt',0,'honeymalt',0,'ambermalt',0,'irishalemalt',0);

list=fieldnames(default);
result=default;
IN=length(list);
i=1;
%reading the user's input
if nargin>1
    %
    %placing inputfields in array of strings
    %
    for j=1:nargin-2;
        if rem(j,2)~=0; % If division of argument number by 2 yeilds a remainder, then argument number is odd.
            chklist{i}=varargin{j}; % Put odd arguments, the 'string' arguments, into cell array of strings.
            i=i+1;
        end
    end
    %
    %Checking which default parameters have to be changed
    % and keep them in the structure 'result'.
    %
    while counter<=IN
        index=strmatch(list(counter,:),chklist,'exact');
        if ~isempty(index) %in case of similarity
            for j=1:nargin-2 %searching the index of the accompanying field
                if rem(j,2)~=0 %fieldnames are placed on odd index
                    if strcmp(chklist{index},varargin{j})
                        I=j;
                    end
                end
            end
            result=setfield(result,chklist{index},varargin{I+1});
            index=[];
        end
        counter=counter+1;
    end
end

% Grain bill
pilsnermalt=            [result.pilsnermalt 37];
darkmunichmalt15l=[result.darkmunichmalt15l 35];
viennamalt=              [result.viennamalt 35];
flakedbarley=          [result.flakedbarley 32];
tworowmalt=              [result.tworowmalt 38];
sixrowmalt=              [result.sixrowmalt 36];
palemalt=                  [result.palemalt 38];
caramelmalt10l=      [result.caramelmalt10l 35];
caramelmalt20l=      [result.caramelmalt20l 35];
caramelmalt30l=      [result.caramelmalt30l 35];
caramelmalt40l=      [result.caramelmalt40l 34];
caramelmalt60l=      [result.caramelmalt60l 34];
caramelmalt80l=      [result.caramelmalt80l 34];
caramelmalt120l=    [result.caramelmalt120l 33];
flakedwheat=            [result.flakedwheat 36];
torrifiedwheat=      [result.torrifiedwheat 36];
whitewheatmalt=      [result.whitewheatmalt 39];
biscuitmalt=            [result.biscuitmalt 35];
victorymalt=            [result.victorymalt 34];
chocolatemalt=        [result.chocolatemalt 28];
blackpatentmalt=    [result.blackpatentmalt 25];
carafaiiimalt=        [result.carafaiiimalt 32];
abbeymalt=                [result.abbeymalt 33];
ryemalt=                    [result.ryemalt 29];
roastedbarleymalt=[result.roastedbarleymalt 25];
simpsongoldenpromisemalt=[result.simpsongoldenpromisemalt 37];
englishpalemalt=    [result.englishpalemalt 37];
chocolatewheatmalt=[result.chocolatewheatmalt 34];
flakedoats=              [result.flakedoats 33];
redwheat=                  [result.redwheat 39];
rawwheat=                  [result.rawwheat 35];
carapils=                  [result.carapils 33];
brownmalt=                [result.brownmalt 35];
blackmalt=                [result.blackmalt 35];
flakedcorn=              [result.flakedcorn 40];
acidulatemalt=        [result.acidulatemalt 27];
potstillmalt=          [result.potstillmalt 38];
goldenpromise=        [result.goldenpromise 37];
munichmalt=              [result.munichmalt 34];
ottermalt=                [result.ottermalt 34];
cararubymalt=          [result.cararubymalt 34];
carawheatmalt=        [result.carawheatmalt 37];
honeymalt=                [result.honeymalt 37];
ambermalt=                [result.ambermalt 35];
irishalemalt=          [result.irishalemalt 37];

% Grain bill in array form
grain=[pilsnermalt; darkmunichmalt15l; viennamalt; flakedbarley; tworowmalt;
    caramelmalt10l; caramelmalt20l; caramelmalt30l; caramelmalt40l;
    caramelmalt60l; caramelmalt80l; caramelmalt120l; flakedwheat;
    torrifiedwheat; whitewheatmalt; biscuitmalt; victorymalt; chocolatemalt;
    blackpatentmalt; carafaiiimalt; palemalt; abbeymalt; ryemalt;
    roastedbarleymalt; simpsongoldenpromisemalt; englishpalemalt;
    sixrowmalt; chocolatewheatmalt; flakedoats; redwheat; rawwheat; carapils;
    brownmalt; blackmalt; flakedcorn; acidulatemalt; potstillmalt; goldenpromise;
    munichmalt; ottermalt; cararubymalt; carawheatmalt; honeymalt; ambermalt;
    irishalemalt];

if sum(grain(:,1))~=tot
    error('All grain not accounted for')
end

% Logic matrix for malts present
A=grain(:,1)==0;
grain(A,:)=[];

% PPGs
ppg=sum(grain(:,1).*grain(:,2));
points=ppg/vol;

output=points;
end