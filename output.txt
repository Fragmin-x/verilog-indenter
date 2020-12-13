module counter(
  input             CLK,
  input             RESET,
  output reg [31:0] COUNT
);
  always @(posedge CLK) begin
    if (RESET == 1'b1) begin
      COUNT <= 32'd0;
    end else begin
      COUNT <= COUNT + 32'd1;
      endcount
    end
  end
endmodule