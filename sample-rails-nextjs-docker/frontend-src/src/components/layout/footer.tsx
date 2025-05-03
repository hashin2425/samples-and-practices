'use client';

import { Box, Container, Typography, Link } from '@mui/material';
import { FC } from 'react';

const Footer: FC = () => {
  return (
    <Box
      component="footer"
      sx={{
        py: 3,
        px: 2,
        mt: 'auto',
        backgroundColor: (theme) => theme.palette.grey[200],
      }}
    >
      <Container maxWidth="lg">
        <Typography variant="body1" color="text.secondary" align="center">
          © {new Date().getFullYear()} Your Company Name
          {' • '}
          <Link color="inherit" href="#">
            Privacy
          </Link>
          {' • '}
          <Link color="inherit" href="#">
            Terms
          </Link>
        </Typography>
      </Container>
    </Box>
  );
};

export default Footer;
