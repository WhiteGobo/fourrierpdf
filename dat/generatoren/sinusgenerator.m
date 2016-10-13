#sinusgenerator.m
clear all; clc;

A = [1, 0.2, 0.7, 0.1, 0.1];
pi=3.141592653;
x= 0:0.1*pi:3*pi;
for k=1:5
	sinus(k,:) = A(k)*sin(k*x);
endfor
gesamtsinus=sinus(1,:);
for k=2:5
	gesamtsinus+=sinus(k,:);
endfor
savedata=zeros(length(x),2);
savedata(:,1) = transpose(x);
savedata(:,2) = transpose(gesamtsinus);
save gesamtsinus.dat savedata
savedata(:,2) = transpose(sinus(1,:));
save amplitude1sinus.dat savedata
savedata(:,2) = transpose(sinus(2,:));
save amplitude2sinus.dat savedata
savedata(:,2) = transpose(sinus(3,:));
save amplitude3sinus.dat savedata
savedata(:,2) = transpose(sinus(4,:));
save amplitude4sinus.dat savedata
savedata(:,2) = transpose(sinus(5,:));
save amplitude5sinus.dat savedata