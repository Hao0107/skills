import fs from 'node:fs/promises';

async function handleFiles() {
  try {
    // 1. Ghi file (Tạo mới hoặc ghi đè nội dung cũ)
    await fs.writeFile('example.txt', 'Xin chào Node.js!', 'utf8');

    // 2. Ghi nối tiếp vào cuối file
    await fs.appendFile('example.txt', '\nDòng nội dung thứ hai.', 'utf8');

    // 3. Đọc toàn bộ nội dung file
    const data = await fs.readFile('example.txt', 'utf8');
    console.log('Nội dung file:\n', data);

    // 4. Đổi tên hoặc di chuyển file
    await fs.rename('example.txt', 'renamed-example.txt');

    // 5. Xóa file
    await fs.unlink('renamed-example.txt');
    console.log('Đã xóa file thành công.');
  } catch (err) {
    console.error('Lỗi xử lý file:', err);
  }
}

handleFiles();
