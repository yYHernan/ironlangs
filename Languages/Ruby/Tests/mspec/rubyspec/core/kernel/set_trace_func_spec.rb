require File.dirname(__FILE__) + '/../../spec_helper'
require File.dirname(__FILE__) + '/fixtures/classes'

describe "Kernel#set_trace_func" do
  it "is a private method" do
    Kernel.should have_private_instance_method(:set_trace_func)
  end
end

describe "Kernel.set_trace_func" do
  it "needs to be reviewed for spec completeness"
end
