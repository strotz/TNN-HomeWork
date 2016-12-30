function best()
   for data = {0.005, 0.01, 0.02, 0.05, 0.07, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 1.0, 1.1, 1.3, 1.5, 2.0, 2.1, 2.6},
      rate = data{1};
      loss = a4_main(300, .02, rate, 1000);
      fprintf('learning rate %f, result: %f\n', rate, loss);
   end
end
