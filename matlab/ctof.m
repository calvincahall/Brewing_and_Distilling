function output=ctof(in,varargin)
% Converts degree C to F if varargin is empty.
% Converts degree F to C if varargin is not empty.

if isempty(varargin)==1
    output=in*(9/5)+32;
elseif length(varargin)>0
    output=(in-32)*(5/9);
end

end