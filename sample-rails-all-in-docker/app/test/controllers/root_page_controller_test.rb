require "test_helper"

class RootPageControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get root_page_index_url
    assert_response :success
  end
end
