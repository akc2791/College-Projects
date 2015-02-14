% extraction of datasets %
Interarrival_time = importdata('Data1.txt'); 
Service = importdata('Data2.txt');

% Transformation of data sets %
Interarrival_time = (-0.9 * log(1-Interarrival_time));
Service = (-0.7 * log(1-Service));
 
 
 % creating the arrival and the departure vectors which will be used later on%
arrival = cumsum(Interarrival_time);
dep = zeros(300,1);
dep(1) = Service(1) + arrival(1);
 
% Waiting time algorithm %
Wt = zeros(300, 1);
Wt(1) = 0;
for i = 2:300
dep(i) = max(arrival(i), dep(i-1)) + Service(i);
Wt(i) = max(dep(i-1)-arrival(i), 0);
end;

 

k=1;
l=1;
sck = 0; % counter for the clock to run the while loop 
swk = 0;
c = 0;
m=1;
Qt = zeros(600, 1);
clock = [];
queue = [];
 
while (sck < max(dep)) % max value in the while loop is set to the fi
%nal dep%    
 if(arrival(k) < dep(l))
  
  sck = arrival(k);   % iteration to change the clock value to arrival %time for object%
  
  if swk == 0
      swk = 1;
       if q>0
           q=q-1;
       else
           q=q;
       end;      
  else
   q=q+1;
  end
% appending the values in an array %
queue = [queue,q];  
clock = [clock,sck];
k=k+1;
 
  m= m+1;
  
 else
  sck = dep(l); % iteration of clock time to departure time of the item 
  c=c+1;
         if q>0
           q=q-1;
       else
        swk = 0; 
       end;  
 queue = [queue,q];
clock = [clock,sck];
 
  
  l=l+1;
 
  m = m+1;
  end;
end;
 
av.n.q = (sum(Wt)/max(dep)) %Average no. of entities
 
a = zeros(600,1);
for i = 1:599 
    if queue(i) >=3
    a(i) = clock(i+1)-clock(i);
    else
    end;
end;

g.t.3 = (sum(a)/max(dep))*100; %percentage of time more than 3 entries in %system%

su = (sum(Service)/max(dep))*100 %server utilization



