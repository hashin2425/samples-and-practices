class CreateExamples < ActiveRecord::Migration[7.1]
  def change
    create_table :examples do |t|
      t.string :title, null: false

      t.timestamps
    end
  end
end
